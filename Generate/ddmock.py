import os
import shutil
import sys
import plistlib
import logging
import json
import argparse

# create the map of endpoints from mockfiles


def generate_map(mockfiles_path):
    endpoint_map = {}

    # walks all the mockfiles and for each creates just the leading path?

    # recursive directory traversal
    # todo: what is subdir
    # damn dynamic types
    for subdir, dirs, files in os.walk(mockfiles_path):
        print(subdir)

        # iterate through mockfiles
        for file in files:

            # create path
            filepath = subdir + os.sep + file

            # only the json files
            if filepath.endswith(".json"):
                endpointPath = subdir.replace(mockfiles_path, "")

                # strip the leading slash if present
                # todo: presumably this is always present? wt
                if endpointPath.startswith("/"):
                    endpointPath = endpointPath.replace("/", "", 1)

                # map is accessed here (therefore make this a function duh)
                if endpointPath in endpoint_map:
                    files = endpoint_map[endpointPath]
                    files.append(file)
                else:
                    endpoint_map[endpointPath] = [file]

    return endpoint_map


def load_root_json():
    with open("Resources/root.json", "r") as root:
        return json.load(root)


def load_endpoint_json():
    with open("Resources/endpoint.json", "r") as endpoint:
        return json.load(endpoint)


def main(mockfiles_path):
    print("wd: " + os.getcwd())

    # first create the map
    # this is where the directory traversal happens
    print("Creating map of endpoint paths and mock files...")
    endpoint_map = generate_map(mockfiles_path)

    # start creating settings bundle
    # todo: what is the settings bundle & where are we creating it?
    print("Creating Settings.bundle...")

    # todo: args in python are weird, need to check their usage

    # todo: dynamic / configuration
    # is this from cwd or root of project?
    # todo: this should come from arguments
    settings_location = "Settings.bundle/"

    # Settings.bundle is really just a directory
    # first create directory if it doesn't exist
    if not os.path.exists(settings_location):
        os.makedirs(settings_location)

    # create root plist
    print("Creating root plist...")
    root = load_root_json()

    print("Creating endpoint plist...")
    endpoint = load_endpoint_json()

    # # Endpoints plist file
    # plist = '<?xml version="1.0" encoding="UTF-8"?>'
    # plist = plist + '\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">'
    # plist = plist + '\n<plist version="1.0">'
    # plist = plist + "\n<dict>"
    # plist = plist + "\n\t<key>PreferenceSpecifiers</key>"
    # plist = plist + "\n\t<array>"
    # plist = plist + "\n\t\t<dict>"
    # plist = plist + "\n\t\t\t<key>Type</key>"
    # plist = plist + "\n\t\t\t<string>PSToggleSwitchSpecifier</string>"
    # plist = plist + "\n\t\t\t<key>Title</key>"
    # plist = plist + "\n\t\t\t<string>Use real API</string>"
    # plist = plist + "\n\t\t\t<key>Key</key>"
    # plist = plist + "\n\t\t\t<string>$endpointPathKey_use_real_api</string>" # $endpointPathKey
    # plist = plist + "\n\t\t\t<key>DefaultValue</key>"
    # plist = plist + "\n\t\t\t<false/>"
    # plist = plist + "\n\t\t</dict>"
    # plist = plist + "\n\t\t<dict>"
    # plist = plist + "\n\t\t\t<key>DefaultValue</key>"
    # plist = plist + "\n\t\t\t<string>$endpointPathName</string>"
    # plist = plist + "\n\t\t\t<key>Type</key>"
    # plist = plist + "\n\t\t\t<string>PSTitleValueSpecifier</string>"
    # plist = plist + "\n\t\t\t<key>Title</key>"
    # plist = plist + "\n\t\t\t<string>Endpoint</string>"
    # plist = plist + "\n\t\t\t<key>Key</key>"
    # plist = plist + "\n\t\t\t<string>$endpointPathKey_endpoint</string>" # $endpointPathKey
    # plist = plist + "\n\t\t</dict>"
    # plist = plist + "\n\t\t<dict>"
    # plist = plist + "\n\t\t\t<key>Type</key>"
    # plist = plist + "\n\t\t\t<string>PSTextFieldSpecifier</string>"
    # plist = plist + "\n\t\t\t<key>DefaultValue</key>"
    # plist = plist + "\n\t\t\t<string>400</string>"
    # plist = plist + "\n\t\t\t<key>Title</key>"
    # plist = plist + "\n\t\t\t<string>Response Time (ms)</string>"
    # plist = plist + "\n\t\t\t<key>Key</key>"
    # plist = plist + "\n\t\t\t<string>$endpointPathKey_response_time</string>" # $endpointPathKey
    # plist = plist + "\n\t\t</dict>"
    # plist = plist + "\n\t\t<dict>"
    # plist = plist + "\n\t\t\t<key>Type</key>"
    # plist = plist + "\n\t\t\t<string>PSTextFieldSpecifier</string>"
    # plist = plist + "\n\t\t\t<key>DefaultValue</key>"
    # plist = plist + "\n\t\t\t<string>200</string>"
    # plist = plist + "\n\t\t\t<key>Title</key>"
    # plist = plist + "\n\t\t\t<string>Status Code</string>"
    # plist = plist + "\n\t\t\t<key>Key</key>"
    # plist = plist + "\n\t\t\t<string>$endpointPathKey_status_code</string>" # $endpointPathKey
    # plist = plist + "\n\t\t</dict>"
    # plist = plist + "\n\t\t<dict>"
    # plist = plist + "\n\t\t\t<key>Type</key>"
    # plist = plist + "\n\t\t\t<string>PSMultiValueSpecifier</string>"
    # plist = plist + "\n\t\t\t<key>Title</key>"
    # plist = plist + "\n\t\t\t<string>Mock file</string>"
    # plist = plist + "\n\t\t\t<key>Key</key>"
    # plist = plist + "\n\t\t\t<string>$endpointPathKey_mock_file</string>" # $endpointPathKey
    # plist = plist + "\n\t\t\t<key>DefaultValue</key>"
    # plist = plist + "\n\t\t\t<real>0</real>"
    # plist = plist + "\n\t\t\t<key>Values</key>"
    # plist = plist + "\n\t\t\t<array>"
    # plist = plist + "\n\t\t\t\t$indexMockFiles"  # $indexMockFiles
    # plist = plist + "\n\t\t\t</array>"
    # plist = plist + "\n\t\t\t<key>Titles</key>"
    # plist = plist + "\n\t\t\t<array>"
    # plist = plist + "\n\t\t\t\t$mockFiles"       # $mockFiles
    # plist = plist + "\n\t\t\t</array>"
    # plist = plist + "\n\t\t</dict>"
    # plist = plist + "\n\t</array>"
    # plist = plist + "\n</dict>"
    # plist = plist + "\n</plist>"

    # ** short circuit for testing

#    with open(settings_location + "Root.plist", "rb") as root:
    # with open("resources/endpoint.json", "w+") as output:
    #     plist_bytes = plist.encode(encoding='utf-8')
    #     plist = plistlib.loads(plist_bytes, fmt=plistlib.FMT_XML)
    #     json.dump(plist, output, indent=4)
    #     print("dumped root json")

    # return

    # **
    # for path & files in map
    for endpointPath, files in endpoint_map.items():

        # replaces the slashes with periods for
        filename = endpointPath.replace("/", ".")

        print(root)

        # add endpoint to root plist
        new_item = {}
        new_item['Type'] = 'PSChildPaneSpecifier'
        new_item['File'] = filename
        new_item['Title'] = filename

        root['PreferenceSpecifiers'].append(new_item)

        # create a copy of the endpoint plist replacing
        # the $endpointPathName key     -> endpointPath
        # the $indexMockFiles key       -> indexes
        # the $mockfiles key            -> files[i]
        # then write the new file at settings_location + filename + .plist

        # creating plist file for endpoint
        print("Creating plist file for " + endpointPath + "...")

        def replaceKeys(item, path, filename):
            # todo: clarify what is happening
            item['DefaultValue'] = item['key'].replace(
                "$endpointPathName", path)
            item['Key'] = item['key'].replace("$endpointPathKey", filename)


        # todo: endpoints added to plist here
        with open(settings_location + filename + ".plist", "wb") as fout:
            new_endpoint = endpoint

            map(lambda item: replaceKeys, new_endpoint["PreferenceSpecifiers"])

            # newplist = newplist.replace("$endpointPathName", endpointPath).replace(
            #     "$endpointPathKey", filename)

            # indexes = "<integer>0</integer>"
            for setting in filter(lambda item: item['Title'] == "Mock file", new_endpoint['PreferenceSpecifiers']):
                setting["Values"] = list(range(0, len(files)))
                setting["Titles"] = files
            #     indexes = indexes + "\n\t\t\t\t<integer>" + \
            #         str(i) + "</integer>"
            # newplist = newplist.replace("$indexMockFiles", indexes)

            # mockFiles = "<string>" + files[0] + "</string>"
            # for i in range(1, len(files)):
            #     mockFiles = mockFiles + "\n\t\t\t\t<string>" + \
            #         files[i] + "</string>"
            # newplist = newplist.replace("$mockFiles", mockFiles)

            plistlib.dump(new_endpoint, fout, fmt=plistlib.FMT_XML)
            # fout.write(new_endpoint)

    # insert: mb generate general plist? even from some config?

    # general_plist_path = "DDMockiOS/DDMockiOS/general.plist"

    # create general plist from json
    # this could be from
    print("Creating general.plist...")
    with open("Resources/general.json", "r") as general:
        with open(os.path.join(settings_location, "general.plist"), "wb") as output:
            plistlib.dump(general.read(), output, fmt=plistlib.FMT_XML)
    # copy static file
    # failing here because it's not from cwd or a variable
    # todo: some var for location
    # copies the "general.plist"
    # todo: generate from the lib
    # shutil.copyfile(general_plist_path,
            # os.path.join(settings_location, "general.plist"))

    # copies from one static path to another (pointlessly?)

    # close the plist
    # root = root + "\n\t</array>"
    # root = root + "\n</dict>"
    # root = root + "\n</plist>"

    # write root plist
    with open(settings_location + "Root.plist", "wb") as output:
        print("Writing root plist...")
        plistlib.dump(root, output, fmt=plistlib.FMT_XML)

    # finished
    print("Done!")


if __name__ == "__main__":

    # parse arguments
    parser = argparse.ArgumentParser(
        description='Generate Settings.bundle for DDMockiOS')
    parser.add_argument('mockfiles_path', nargs='?',
                        default="DDMockiOS/resources/mockfiles")

    args = parser.parse_args()

    # start execution
    main(args.mockfiles_path)
