import re
import urllib2

from autopkglib import Processor, ProcessorError


__all__ = ["DeployStudioURLProvider"]


# http://www.deploystudio.com/Downloads/_dss.current
# http://www.deploystudio.com/get.php?fp=DeployStudioServer_v1.6.3.dmg

class DeployStudioURLProvider(Processor):
    description = "Provides URL to the latest DeployStudio download."
    input_variables = {
    }
    output_variables = {
        "version": {
            "description": "Version of the DeployStudio download.",
        },
        "url": {
            "description": "URL to the latest DeployStudio release download.",
        },
    }
    
    __doc__ = description
    
    def main(self):        
        self.env["version"] = "1.6.3"
        self.output("Found version %s" % self.env["version"])
        self.env["filename"] = "DeployStudioServer_v1.6.3.dmg"
        self.output("Found download filename %s" % self.env["filename"])
        self.env["url"] = "http://www.deploystudio.com/get.php?fp=DeployStudioServer_v1.6.3.dmg"
        self.output("Found URL %s" % self.env["url"])


if __name__ == "__main__":
    processor = DeployStudioURLProvider()
    processor.execute_shell()