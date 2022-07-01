// swift-tools-version: 5.6
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "ddmock-ios",
    platforms: [.iOS(.v11)],
    products: [
        .library(
            name: "ddmock-ios",
            targets: ["ddmock-ios"]),
    ],
    dependencies: [],
    targets: [
        .target(
            name: "ddmock-ios",
            dependencies: [],
            path: "Sources"
        ),
        .testTarget(
            name: "ddmock-iosTests",
            dependencies: ["ddmock-ios"],
            path: "Tests"
        ),
    ]
)
