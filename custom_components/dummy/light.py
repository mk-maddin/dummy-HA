"""Demo light platform that implements lights."""
import logging
import random

## DemoLight class
from homeassistant.components.light import (
    ATTR_BRIGHTNESS,
    ATTR_COLOR_TEMP,
    ATTR_EFFECT,
    ATTR_HS_COLOR,
    ATTR_WHITE_VALUE,
    SUPPORT_BRIGHTNESS,
    SUPPORT_COLOR,
    SUPPORT_COLOR_TEMP,
    SUPPORT_EFFECT,
    SUPPORT_WHITE_VALUE,
    Light,
)
from homeassistant.components.demo.light import DemoLight

from homeassistant.const import (
#    CONF_LIGHTS,
    CONF_NAME,
    CONF_ENTITY_ID,
    CONF_STATE,
    STATE_ON,
    STATE_OFF,
    STATE_UNKNOWN,
)
from . import (
    DOMAIN,
    CONF_LIGHTS,
    CONF_AVAILABLE,
    DEFAULT_AVAILABLE,
)

_LOGGER = logging.getLogger(__name__)

states=[STATE_ON,STATE_OFF,STATE_UNKNOWN]


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the dummy light platform."""
    domain=CONF_LIGHTS
    devices=[]
    
    _LOGGER.debug("Create dummy %s enties", domain)
    for entity in hass.data[DOMAIN][domain]:
        if not CONF_STATE in entity:
            _LOGGER.debug("Add %s property to entity", CONF_STATE)
            entity[CONF_STATE]=random.choice(states)
        
        if not CONF_AVAILABLE in entity:
            _LOGGER.debug("Add %s property to entity", CONF_AVAILABLE)
            entity[CONF_AVAILABLE]=DEFAULT_AVAILABLE
       
        _LOGGER.debug("Create demo %s entity: %s", domain, entity)
        #class:        DemoLight(unique_id,name,state,available=False,hs_color=None,ct=None,brightness=180,white=200,effect_list=None,effect=None)
        #example:      DemoLight("light_2", "Ceiling Lights", True, True, LIGHT_COLORS[0], LIGHT_TEMPS[1])
        devices.append(DemoLight(entity[CONF_ENTITY_ID],entity[CONF_NAME],entity[CONF_STATE],entity[CONF_AVAILABLE]))
    
    add_entities(devices)
    _LOGGER.debug("setup_platform: %s complete!", domain)

