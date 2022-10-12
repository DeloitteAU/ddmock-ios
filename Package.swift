// swift-tools-version: 5.6
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "DDMock",
    platforms: [.iOS(.v11)],
    products: [
        .library(
            name: "DDMock",
            targets: ["DDMock"]),
    ],
    dependencies: [],
    targets: [
        .target(
            name: "DDMock",
            dependencies: []
        ),
        .testTarget(
            name: "DDMockTests",
            dependencies: ["DDMock"]
        ),
    ]
)
