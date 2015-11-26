{
    "includes": [
        "common.gypi"
    ],
    "targets": [
        {
            "target_name": "mylib",
            "product_name": "mylib",
            "type": "static_library",
            "sources": [
                "src/implementation.cc",
                "include/mylib/interface.h"
            ],
            "include_dirs": [
                "include"
            ],
            'direct_dependent_settings': {
              'include_dirs': [ 'include/' ],
            }
        },
        {
            "target_name": "myapp",
            "type": "executable",
            "sources": [
                "./bin/myapp.cc"
            ],
            "dependencies": [
                "mylib"
            ]
        }
    ]
}
