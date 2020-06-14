"""Support for custom dummy devices"""
import logging
import voluptuous as vol

from homeassistant.const import (
    CONF_PLATFORM,
#    CONF_LIGHTS,
#    CONF_SWITCHES,
#    CONF_COVERS,
    CONF_NAME,
    CONF_ENTITY_ID,
    CONF_STATE,
    CONF_ICON,
    ATTR_ASSUMED_STATE,    
    STATE_ON,
    STATE_OFF,
)
from homeassistant.helpers import discovery
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

CONF_AVAILABLE='available'
CONF_LIGHTS='light'
CONF_SWITCHES='switch'
CONF_COVERS='cover'

DOMAIN = 'dummy'
SUPPORTED_DOMAINS = [CONF_LIGHTS,CONF_SWITCHES,CONF_COVERS]

DEFAULT_STATE=STATE_OFF
DEFAULT_AVAILABLE=True
DEFAULT_ICON=None
DEFAULT_ASSUMED=False

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            cv.ensure_list,
            [
                vol.Schema(
                    {
                    vol.Required(CONF_PLATFORM): vol.In([CONF_LIGHTS,CONF_SWITCHES,CONF_COVERS]),
                    vol.Required(CONF_ENTITY_ID): cv.string,
                    vol.Required(CONF_NAME): cv.string,
                    vol.Optional(CONF_STATE): vol.In([STATE_ON,STATE_OFF]),
                    vol.Optional(CONF_AVAILABLE): vol.In([True,False]),
                    }
                )
            ],
        )
    },
    extra=vol.ALLOW_EXTRA,
)

def setup(hass, config):
    """Setup the dummy component."""
    hass.data[DOMAIN]={}
    for domain in SUPPORTED_DOMAINS:
        _LOGGER.debug("Discover platform: %s - %s",DOMAIN, domain)
        hass.data[DOMAIN][domain]=[]
        for entity in config[DOMAIN]:
            if entity['platform'] == domain:
                hass.data[DOMAIN][domain].append(entity)
        discovery.load_platform(hass, domain, DOMAIN, {}, config)

    # Return boolean to indicate that initialization was successful.
    _LOGGER.debug("The '%s' component is ready!", DOMAIN)
    return True

