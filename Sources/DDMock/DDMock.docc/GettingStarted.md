# Getting Started With DDMock

## Initialisation

1. Add `DDMock.shared.initialise()` to AppDelegate

2. Add `DDMockProtocol.initialise(config: ...)` to networking library/initialisation

e.g.

```swift
let configuration = URLSessionConfiguration.default
// other configuration set up
DDMockProtocol.initialise(config: configuration)
```

3. Check if after first run of the app, the `Settings.bundle` file underneath the `DDMock/` is added to the project. If not add this to the project.

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

You must pass the `URLSessionConfiguration` used for ``DDMockProtocol`` into your networking layer after the ``DDMockProtocol/initialise(config:)`` call for DDMock to be active. If you create a `URLSession` with the `URLSessionConfiguration` used before the ``DDMockProtocol/initialise(config:)`` call, then DDMock will not be active.
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

## Topics

### <!--@START_MENU_TOKEN@-->Group<!--@END_MENU_TOKEN@-->

- <!--@START_MENU_TOKEN@-->``Symbol``<!--@END_MENU_TOKEN@-->
