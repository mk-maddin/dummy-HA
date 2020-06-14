"""Demo cover platform that implements covers."""
import logging
import random

## DemoCover class
from homeassistant.helpers.event import track_utc_time_change
from homeassistant.components.cover import (
    ATTR_POSITION,
    ATTR_TILT_POSITION,
    SUPPORT_CLOSE,
    SUPPORT_OPEN,
    CoverDevice,
)
from homeassistant.components.demo.cover import DemoCover

from homeassistant.const import (
#    CONF_COVERS,
    CONF_NAME,
    CONF_ENTITY_ID,
    STATE_CLOSED,
    STATE_OPEN
)
from . import (
    DOMAIN,
    CONF_COVERS,
)

_LOGGER = logging.getLogger(__name__)

states=[STATE_CLOSED,STATE_OPEN]

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the dummy cover platform."""
    domain=CONF_COVERS
    devices=[]

    _LOGGER.debug("Create dummy %s enties", domain)
    for entity in hass.data[DOMAIN][domain]:
        _LOGGER.debug("Create demo %s entity: %s", domain, entity)
        #class:        DemoCover(hass,unique_id,name,position=None,tilt_position=None,device_class=None,supported_features=None)
        #example:      DemoCover(hass, "cover_3", "Living Room Window", 70, 50)
        devices.append(DemoCover(hass,entity[CONF_ENTITY_ID],entity[CONF_NAME]))
    
    add_entities(devices)
    _LOGGER.debug("setup_platform: %s complete!", domain)

