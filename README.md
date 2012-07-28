=======
jsonfig
=======

Simple autoreloading configuration files in JSON. Will use the very fast UltraJSON library for parsing if available.

Installation
============

    $ pip install jsonfig

Usage
=====

Create a JSON file whose root is a dictionary:

    {
        "always_load_user_data": true,
        "use_new_feature_123": false,
        "feature_456_chance": 0.20
    }

Now it can be loaded as a dictionary:

    >>> config = jsonfig.from_path("example.json")
    >>> config["feature_456_chance"]
    0.20

By default, when the file is changed, it will be automatically reloaded within one second:

    {
        "always_load_user_data": true,
        "use_new_feature_123": false,
        "feature_456_chance": 1.0
    }

Now the new value will show up in the config structure:

    >>> config["feature_456_chance"]
    1.0
