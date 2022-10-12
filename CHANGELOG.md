# Change Log
All notable changes to this project will be documented in this file.
`DDMock` adheres to [Semantic Versioning](https://semver.org/).

#### 0.x Releases
- `0.x` Releases - [0.1.4](#014) | [0.1.5](#015) | [0.1.6](#016) | [0.1.7](#017) | [0.2.0](#020)

---
## [0.2.0](https://github.com/DeloitteDigitalAPAC/ddmock-ios/releases/tag/v0.2.0)
Released on 2022-07-19

#### Updated
- Refactored project to be called DDMock instead of DDMockiOS and ddmock-ios

## [0.1.7](https://github.com/DeloitteDigitalAPAC/ddmock-ios/releases/tag/v0.1.7)
Swift Package only
Released on 2022-07-13

#### Added
- Added Swift Package Manager support

## [0.1.6](https://github.com/DeloitteDigitalAPAC/ddmock-ios/releases/tag/v0.1.6)
Released on 2022-06-10

#### Added
- Added optional `X-Mocked-By: DDMock <version>` header to make it easier to debug when a response is being mocked
- Added Strict mode which will trigger a closure when a mock is missing for a request
- Added CocoaPod support

#### Updated
- Updated init-mock.py to Python 3 due to MacOS dropping support for Python 2
- Updated Framework build script to build XCFrameworks for Xcode 11+ compatibility

## [0.1.5](https://github.com/DeloitteDigitalAPAC/ddmock-ios/releases/tag/v0.1.5)
Released on 2020-05-01

#### Added
- Added Global Use Real APIs toggle

#### Fixed
- Fixed an issue with regex

## [0.1.4](https://github.com/DeloitteDigitalAPAC/ddmock-ios/releases/tag/v0.1.4)
Released on 2020-04-30
Initial public version
