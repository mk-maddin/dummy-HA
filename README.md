[dummy Custom Component](https://github.com/mk-maddin/dummy-HA) for homeassistant

# What This Is:

This is a custom component which creates dummy devices in [Homeassistant](https://home-assistant.io).
These can be used for tests, development or other tasks.

# What It Does:

Creates dummy entities of different domains within Home Assistant.

# Installation and Configuration

## Installation
Download the repository and save the "dummy" folder into your home assistant custom_components directory.

## Configuration
Once the files are downloaded, you’ll need to **update your config** to create entities under the **`dummy` domain**.
Obviously you can create multiple entities of the same domain or mix differnt domains.

### cover
```yaml
dummy:
  - platform: cover
    entity_id: my_cover1
    name: My Dummy Cover
```

### light
```yaml
dummy:
  - platform: light
    entity_id: my_light1
    name: My Dummy Light
```

### switch
```yaml
dummy:
  - platform: switch
    entity_id: my_switch1
    name: My Dummy Switch
```

# License

[Apache-2.0](LICENSE). By providing a contribution, you agree the contribution is licensed under Apache-2.0. This is required for Home Assistant contributions.
