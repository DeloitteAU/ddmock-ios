![Deloitte Digital](https://raw.githubusercontent.com/DeloitteDigitalAPAC/ddmock-ios/master/dd-logo.png)

# DDMock

[![Version](https://img.shields.io/cocoapods/v/DDMock.svg?style=flat)](https://cocoapods.org/pods/DDMock)
[![License](https://img.shields.io/cocoapods/l/DDMock.svg?style=flat)](https://cocoapods.org/pods/DDMock)
[![Platform](https://img.shields.io/cocoapods/p/DDMock.svg?style=flat)](https://cocoapods.org/pods/DDMock)

## Table of Contents

- [What?](#what-is-this)
- [Requirements](#requirements)
- [Installation](#installation)
  - [CocoaPods](#cocoapods)
  - [Swift Package Manager](#swift-package-manager)
  - [Building from scratch](#building-from-scratch)
- [Configuration](#configuration)
  - [Initialisation](#initialisation)
  - [Build configuration-specific configuration](#build-configuration-specific-configuration)
- [Usage](#usage)
  - [Options](#options)
- [Mock files](#mock-files)
- [Notes/Troubleshooting](#notestroubleshooting)
- [Known Issues](#known-issues)
- [Changelog](#changelog)
- [License](#license)

## What is this?

DDMock is an API mocking library designed around the use of embedded JSON files

## Requirements

- Python 3
- iOS 11+

## Installation

DDMock can be installed via these methods:

- [CocoaPods](#cocoapods)
- [Swift Package Manager](#swift-package-manager)
- [Building from scratch](#building-from-scratch)

### CocoaPods

DDMock is available through [CocoaPods](https://cocoapods.org).

1. Add the following line to your Podfile:

```ruby
pod 'DDMock'
```

2. Run `pod install`

3. Click on your project in the file list, choose your target under `TARGETS`, click the `Build Phases` tab

4. Add a `New Run Script Phase` by clicking the little plus icon in the top left

5. Drag the new `Run Script` phase **above** the `Compile Sources` phase, expand it and paste the following script:

```bash
if [ $ENABLE_PREVIEWS = NO ]; then
    python3 "${PODS_ROOT}/DDMock/init-mocks.py" "<path_to_mock_files_directory>/mockfiles"
fi
```

### Swift Package Manager

1. Add https://github.com/DeloitteDigitalAPAC/ddmock-ios url as a Swift package as described in https://developer.apple.com/documentation/xcode/adding-package-dependencies-to-your-app for adding it to an app or https://developer.apple.com/documentation/xcode/creating-a-standalone-swift-package-with-xcode#Add-a-dependency-on-another-Swift-package for adding it to another Swift package.

2. Click on your project in the file list, choose your target under `TARGETS`, click the `Build Phases` tab

3. Add a `New Run Script Phase` by clicking the little plus icon in the top left

4. Drag the new `Run Script` phase **above** the `Compile Sources` phase, expand it and paste the following script:

```bash
if [ $ENABLE_PREVIEWS = NO ]; then
    python3 "${BUILD_DIR%Build/*}SourcePackages/checkouts/DDMock/init-mocks.py" "<path_to_mock_files_directory>/mockfiles"
fi
```

### Building from scratch

1. Clone repository and run `sh build-xcframework.sh`

```bash
$ git clone https://github.com/DeloitteDigitalAPAC/ddmock-ios
$ cd ddmock-ios
$ sh build-xcframework
```

2. Framework should be created in `output/DDMock`

3. Drag `output/DDMock/` into project root folder

4. Click on your project in the file list, choose your target under `TARGETS`, click the `Build Phases` tab

5. Add a `New Run Script Phase` by clicking the little plus icon in the top left

6. Drag the new `Run Script` phase **above** the `Compile Sources` phase, expand it and paste the following script:

```bash
if [ $ENABLE_PREVIEWS = NO ]; then
    python3 "${SRCROOT}/DDMock/init-mocks.py" "<path_to_mock_files_directory>/mockfiles"
fi
```

## Configuration

### Initialisation

1. Add `DDMock.shared.initialise()` to AppDelegate

2. Add `DDMockProtocol.initialise(config: ...)` to networking library/initialisation

e.g.

```swift
let configuration = URLSessionConfiguration.default
// other configuration set up
DDMockProtocol.initialise(config: configuration)
```

3. Check if after first run of the app, the `Settings.bundle` file underneath the `DDMock/` is added to the project. If not add this to the project.

### Build configuration-specific configuration

To use DDMock in only some build configurations (e.g. Test), you must add a custom compilation condition flag to the build settings (if one doesn't already exist for the build configurations you want to use) and surround the initialisation calls for DDMock with a `#if <flag> #endif` block.
Additionally you can set the mockfiles to only be included in some build configurations (e.g. to avoid including them unnecessarily in a Store build) by using a build phase script

1. Navigate to the Build Settings for your app target (or project if you want to add it to all of your targets)

2. Scroll down to Active Compilation Conditions in the Swift Compiler - Custom Flags section (if you can't see it, make sure Customized is not selected at the top) or type `Active Compilation Conditions` into the filter field

3. Double click the field in the row for the configuration you want to add the flag to (e.g. Debug) and click +

4. Type in a unique name for the compilation flag (e.g. `TEST` or `MOCK`)

5. Follow steps 3 & 4 for any other build configurations you want DDMock in

6. Navigate to where you have added initialisation code or imports for DDMock and DDMockProtocol and surround the code in `#if <flag> #endif` blocks
e.g.
```diff
+ #if MOCK
import DDMockiOS
+ #endif

// ... Other code ...

+ #if MOCK
DDMock.shared.initialise()
+ #endif
```

7. Add a new `Run Script Phase` to the targets you want to use DDMock with and put it after Copy Bundle Resources phase and put this script:
```bash
if [ "${CONFIGURATION}" != "Store" ]; then # Modify check to match configurations you want to use DDMock with
    echo "Copying DDMock settings"
    cp -r "${PROJECT_DIR}/DDMockiOS/Settings.bundle" "${BUILT_PRODUCTS_DIR}/${PRODUCT_NAME}.app"
    cp -r "<path_to_mock_files_directory>/mockfiles" "${BUILT_PRODUCTS_DIR}/${PRODUCT_NAME}.app"
else
    echo "Skip copying DDMock settings on Store"
fi
```

## Usage

Once you have installed an app using DDMock, you can navigate to the Settings app and scroll down to the app, then tap on it. Changes will take effect on next API call.

### Options

- Use real APIs - Select to bypass DDMock for all endpoints (default: `false`)
- Mocks - Allows you to set individual settings and selected mock file for each mocked endpoint
    - Use real API - Select to bypass DDMock for this endpoint (default: `false`)
    - Response Time - How long before the DDMock returns the response (default: `400` ms)
    - Status Code - HTTP Status Code to return (default: `200`)
    - Mock file - Select which mock file to use


## Mock files

- All mock files must be stored under a directory called **/mockfiles**.
- The **/mockfiles** must be a folder reference and not a group and stored under the **Resources** folder
- All mock files are mapped based on the **endpoint path** and **HTTP method**.
- e.g. login mock response file for endpoint **POST** BASE_URL/**mobile-api/v1/auth/login** should be stored under **mobile-api/v1/auth/login/post**
- For dynamic endpoint url, create directories with **\_** and **\_** for every replacement blocks and parameters
- e.g. mock files for **GET** BASE_URL/**mobile-api/v1/users/\_usersId\_** should be stored under **mobile-api/v1/users/{usersId}/get**
- see `sample`
- All mock files need to be JSON files
- There can be more than one mock file stored under each endpoint path
- By default, the first file listed (alphabetically ordered) under each endpoint path is selected as the mock response

## Notes/Troubleshooting

You must pass the `URLSessionConfiguration` used for `DDMockProtocol` into your networking layer after the `DDMockProtocol.initialise` call for DDMock to be active. If you create a `URLSession` with the `URLSessionConfiguration` used before the `DDMockProtocol.initialise` call, then DDMock will not be active.
Working Example:

```swift
// session config
let config = URLSessionConfiguration.default

// init DDMock
DDMock.shared.initialise()
// this function is mutating
DDMockProtocol.initialise(config: config)

let session = URLSession(
    configuration: config,
    delegate: self,
    delegateQueue: OperationQueue.main
)
```

## Known Issues

- Mismatch between selected mock file and displayed mock file.

    Sometimes adding/renaming mock files will cause the sort order for mock files in the filesystem to not match the sort order for mock files in Settings app, which will cause DDMock to use the wrong mock file.

- Inability to disable DDMock by default

## Changelog

Release notes and changes are in [CHANGELOG.md](CHANGELOG.md)


## License

MIT License

Copyright (c) 2022 Deloitte Digital

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
