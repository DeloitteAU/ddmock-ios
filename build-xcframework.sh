#!/bin/sh

#  build-xcframework.sh
#  

# Prints the archive path for simulator
function archivePathSimulator {
local DIR=output/archives/"${1}-SIMULATOR"
echo "${DIR}"
}
# Prints the archive path for device
function archivePathDevice {
local DIR=output/archives/"${1}-DEVICE"
echo "${DIR}"
}
# Archive takes 3 params
#
# 1st == SCHEME
# 2nd == destination
# 3rd == archivePath
function archive {
echo "📨 Starts archiving the scheme: ${1} for destination: ${2};\n📝 Archive path: ${3}.xcarchive"
xcodebuild archive \
-project DDMock.xcodeproj \
-scheme ${1} \
-destination "${2}" \
-archivePath "${3}" \
SKIP_INSTALL=NO \
BUILD_LIBRARY_FOR_DISTRIBUTION=YES | xcpretty
}
# Builds archive for iOS/tvOS simulator & device
function buildArchive {
SCHEME=${1}
archive $SCHEME "generic/platform=iOS Simulator" $(archivePathSimulator $SCHEME)
archive $SCHEME "generic/platform=iOS" $(archivePathDevice $SCHEME)
}
# Creates xc framework
function createXCFramework {
FRAMEWORK_ARCHIVE_PATH_POSTFIX=".xcarchive/Products/Library/Frameworks"
FRAMEWORK_SIMULATOR_DIR="$(archivePathSimulator $1)${FRAMEWORK_ARCHIVE_PATH_POSTFIX}"
FRAMEWORK_DEVICE_DIR="$(archivePathDevice $1)${FRAMEWORK_ARCHIVE_PATH_POSTFIX}"
xcodebuild -create-xcframework \
-framework ${FRAMEWORK_SIMULATOR_DIR}/${1}.framework \
-framework ${FRAMEWORK_DEVICE_DIR}/${1}.framework \
-output output/xcframeworks/${1}.xcframework
}

# Make xcpretty optional
if ! command -v xcpretty > /dev/null; then
    function xcpretty {
        cat
    }
fi

echo "🚀 Process started 🚀"
echo "📂 Evaluating Output Dir"
mkdir -p output/DDMock
echo "🧼 Cleaning the Output Dir"
rm -rf output/DDMock/DDMock.xcframework
rm -rf output/xcframeworks
rm -rf output/archives
echo "📝 Archive DDMock"
buildArchive DDMock
echo "🗜 Create DDMock.xcframework"
createXCFramework DDMock
mv output/xcframeworks/DDMock.xcframework output/DDMock/DDMock.xcframework
rm -rf output/xcframeworks
rm -rf output/archives
cp init-mocks.py output/DDMock
