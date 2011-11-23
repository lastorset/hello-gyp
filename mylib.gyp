
{
  'targets': [

    {
      'target_name': 'mylib',
      'product_name': 'mylib',
      'type': 'static_library',
      'sources': [
        'src/implementation.cc',
      ],
      'include_dirs': [
         'include',
      ],
    },

    {
      'target_name': 'myapp',
      'type': 'executable',
      'sources': [
        './bin/myapp.cc',
      ],
      'include_dirs': [
         'include',
      ],
      'dependencies': [
        'mylib'
      ],
    },

    {
      'target_name': 'modulename',
      'product_name': 'modulename',
      'type': 'loadable_module',
      'product_prefix': '',
      'product_extension':'node',
      'sources': [
                   "node-addon/modulename.cpp",
      ],
      'include_dirs': [
         'c:\\dev2\\node\\src',
         'c:\\dev2\\node\\deps\\uv\\include',
         'c:\\dev2\\node\\deps\\v8\\include',
      ],
      'ldflags': [
      ],
      'cflags' : [
      ],
      'defines': [
        'PLATFORM="<(OS)"',
        '_LARGEFILE_SOURCE',
        '_FILE_OFFSET_BITS=64',
        #'WIN32',
        #'_WINDOWS',
        #'_USRDLL',
        #'BUILDING_NODE_EXTENSION'
      ],
      'conditions': [
        [ 'OS=="mac"', {
          'libraries': [ '-undefined dynamic_lookup' ],
        }],
        [ 'OS=="win"', {
          'defines': [
            'PLATFORM="win32"',
          ],
          'libraries': [ 'node.lib' ],
          'msvs_settings': {
            'VCLinkerTool': {
              'AdditionalLibraryDirectories': [
                'c:\\dev2\\node\\Debug',
              ],
          },
        },
      }],
      ]
  }
  ],
}