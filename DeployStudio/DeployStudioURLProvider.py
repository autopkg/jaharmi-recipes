#!/usr/bin/env python

import urllib2

from autopkglib import Processor, ProcessorError


__all__ = ["DeployStudioURLProvider"]

# URL to consult for current version of DeployStudio
# http://www.deploystudio.com/Downloads/_dss.current
update_url = "http://www.deploystudio.com/Downloads/_dss.current"

# Sample URL to download a specific version of DeployStudio
# http://www.deploystudio.com/get.php?fp=DeployStudioServer_v1.6.3.dmg


class DeployStudioURLProvider(Processor):
    description = "Provides URL to the latest DeployStudio download."
    input_variables = {
    }
    output_variables = {
        "version": {
            "description": "Version of the DeployStudio download.",
        },
        "filename": {
            "description": "Filename of the latest DeployStudio release download.",
        },
        "url": {
            "description": "URL to the latest DeployStudio release download.",
        },
    }

    __doc__ = description

    def get_deploystudio_version(self, update_url):
        """Find the latest version of DeployStudio and output as a string."""
        try:
            f = urllib2.urlopen(update_url)
            html = f.read()
            # The version is currently the only string in the text file at the
            # update URL, so capture that string
            # If this should change in the future or more error checking is desired,
            # perform more processing here
            download_version_string = html.strip()
            f.close()
        except BaseException as e:
            raise ProcessorError("Can't download %s: %s" % (update_url, e))
        return download_version_string

    def get_deploystudio_dmg_file(self, download_version):
        """Construct the name of the DeployStudio disk image file used in
        the download URL."""
        dmg_filename = "DeployStudioServer_v{0}.dmg".format(download_version)
        return dmg_filename

    def get_deploystudio_dmg_url(self, download_filename):
        """Construct the URL for the DeployStudio file download."""
        # Return URL
        dmg_url = "http://www.deploystudio.com/get.php?fp={0}".format(download_filename)
        return dmg_url

    def main(self):
        """Find and return a download URL."""

        # Get the string representing the requested DeployStudio version
        download_version = self.get_deploystudio_version(update_url)
        self.env["version"] = download_version
        self.output("Found version %s" % self.env["version"])

        # Get the filename of the DeployStudio disk image download using the version
        download_filename = self.get_deploystudio_dmg_file(download_version)
        self.env["filename"] = download_filename
        self.output("Found download filename %s" % self.env["filename"])

        # Get the URL of the DeployStudio disk image download using the filename
        download_url = self.get_deploystudio_dmg_url(download_filename)

        self.env["url"] = download_url
        self.output("Found URL %s" % self.env["url"])


if __name__ == "__main__":
    processor = DeployStudioURLProvider()
    processor.execute_shell()
