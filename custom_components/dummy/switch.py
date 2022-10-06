"""Demo switch platform that implements switches."""
import logging

## DemoSwitch class
from homeassistant.const import DEVICE_DEFAULT_NAME
from homeassistant.components.demo.switch import DemoSwitch

from homeassistant.const import (
#    CONF_SWITCHES,
    CONF_NAME,
    CONF_ENTITY_ID,
    CONF_STATE,
    ATTR_ASSUMED_STATE,
)
from . import (
    DOMAIN,
    CONF_SWITCHES,
    CONF_ICON,
    DEFAULT_STATE,
    DEFAULT_ICON,
    DEFAULT_ASSUMED,
)

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the dummy light platform."""
    domain=CONF_SWITCHES
    devices=[]
    
    _LOGGER.debug("Create dummy %s enties", domain)
    for entity in hass.data[DOMAIN][domain]:
        if not CONF_STATE in entity:
            _LOGGER.debug("Add %s property to entity", CONF_STATE)
            entity[CONF_STATE]=DEFAULT_STATE
       
        if not CONF_ICON in entity:
            _LOGGER.debug("Add %s property to entity", CONF_ICON)
            entity[CONF_ICON]=DEFAULT_ICON
        
        if not ATTR_ASSUMED_STATE in entity:
            _LOGGER.debug("Add %s property to entity", ATTR_ASSUMED_STATE)
            entity[ATTR_ASSUMED_STATE]=DEFAULT_ASSUMED

        _LOGGER.debug("Create demo %s entity: %s", domain, entity)
        #class:        DemoSwitch(unique_id, name, state, icon, assumed, device_class=None)
        #example:      DemoSwitch("swith1", "Decorative Lights", True, None, True)
        devices.append(DemoSwitch(entity[CONF_ENTITY_ID],entity[CONF_NAME],entity[CONF_STATE],entity[CONF_ICON],entity[ATTR_ASSUMED_STATE]))

    add_entities(devices)
    _LOGGER.debug("setup_platform: %s complete!", domain)

