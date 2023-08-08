# SMU-Omniverse

## Getting started with Omniverse

Download Omniverse from here: https://www.nvidia.com/en-us/omniverse/download/. Once you have the Omniverse launcher running, go to the exchange tab and install the Code app (the Isaac Sim app also contains the Script Editor but has more robotics-related features, so I've found it easier to deal with Code).

Pixar's Universal Scene Description (USD) is the primary scene descriptor used by Nvidia Omniverse. Any programs that can export in USD should be able to import into Omniverse. The dancing alien stage I use is provided as `alien.usd`.

For example, if you want to import an asset from Blender, Nvidia built a branch of Blender v4.0 (currently in alpha) with improved USD exporting functionality. You can download it at: https://builder.blender.org/download/experimental/universal-scene-description/ and select the version for your operating system. This guide from Nvidia shows you the process for exporting a USD file from Blender (v3.6 but still applicable) and importing it to Omniverse: https://docs.omniverse.nvidia.com/con_connect/con_connect/blender.html. The documentation for exporting this from Blender is here: https://docs.blender.org/manual/en/4.0/files/import_export/usd.html.

## Notes

You may run `pip install -r requirements.txt` in your environment.

The .vscode directory isn't necessary, but prevents the `import omni` statements from being shown as an error in VSCode. It uses the `app` symlink to link to an Omniverse install (Code, Isaac, etc) to get the omni packages. This is only functionally necessary if you are running Omniverse code outside of the Script Editor, which I am not (yet). I would recommend changing the symlink to your path, again, to make it easier to use VSCode.

The `scripts` directory contains scripts that you can use in the Script Editor inside of Omniverse Code (or Isaac Sim). More info in the `scripts` Readme.

The `tools` directory contains standalone Python scripts for creating a RGBD images, and subsequently point clouds, from the sensor data generated. More info in the `tools` Readme.