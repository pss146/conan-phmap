#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools

class ParallelHashMapConan(ConanFile):
    name = "parallel-hashmap"
    version = "1.24"
    description = "A header-only, very fast and memory-friendly hash map."
    url = "https://github.com/pss146/conan-phmap"
    homepage = "https://github.com/greg7mdp/parallel-hashmap"
    author = "Stanislav Perepelitsyn <stas.perepel@gmail.com>"
    license = "MIT"
    exports = ["LICENSE.md"]
    no_copy_source = True
    source_subfolder = "source_subfolder"

    def source(self):
        tools.get("{0}/archive/{1}.tar.gz".format(self.homepage, self.version))
        extracted_dir = self.name + '-' + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def package(self):
        include_folder = os.path.join(self.source_subfolder, "parallel_hashmap")
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        self.copy(pattern="*", dst="include/parallel_hashmap", src=include_folder)

    def package_id(self):
        self.info.header_only()