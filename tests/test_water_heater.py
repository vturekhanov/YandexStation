from homeassistant.components.water_heater import WaterHeaterEntityFeature

from custom_components.yandex_station.water_heater import YandexKettle
from . import true, false, null, update_ha_state


def test_polaris():
    device = {
        "id": "xxx",
        "name": "Чайник",
        "type": "devices.types.cooking.kettle",
        "icon_url": "https://avatars.mds.yandex.net/get-iot/icons-devices-devices.types.cooking.kettle.svg/orig",
        "capabilities": [
            {
                "retrievable": true,
                "type": "devices.capabilities.on_off",
                "state": {"instance": "on", "value": true},
                "parameters": {"split": false},
            },
            {
                "retrievable": true,
                "type": "devices.capabilities.range",
                "state": {"instance": "temperature", "value": 65},
                "parameters": {
                    "instance": "temperature",
                    "name": "температура",
                    "unit": "unit.temperature.celsius",
                    "random_access": true,
                    "looped": false,
                    "range": {"min": 30, "max": 100, "precision": 5},
                },
            },
            {
                "retrievable": false,
                "type": "devices.capabilities.mode",
                "state": {"instance": "tea_mode", "value": "black_tea"},
                "parameters": {
                    "instance": "tea_mode",
                    "name": "чай",
                    "modes": [
                        {"value": "white_tea", "name": "Белый чай"},
                        {"value": "green_tea", "name": "Зеленый чай"},
                        {"value": "red_tea", "name": "Красный чай"},
                        {"value": "herbal_tea", "name": "Травяной чай"},
                        {"value": "flower_tea", "name": "Цветочный чай"},
                        {"value": "puerh_tea", "name": "Чай пуэр"},
                        {"value": "oolong_tea", "name": "Чай улун"},
                        {"value": "black_tea", "name": "Черный чай"},
                    ],
                },
            },
            {
                "retrievable": true,
                "type": "devices.capabilities.toggle",
                "state": {"instance": "mute", "value": false},
                "parameters": {"instance": "mute", "name": "без звука"},
            },
            {
                "retrievable": true,
                "type": "devices.capabilities.toggle",
                "state": {"instance": "keep_warm", "value": false},
                "parameters": {
                    "instance": "keep_warm",
                    "name": "поддержание тепла",
                },
            },
            {
                "retrievable": true,
                "type": "devices.capabilities.toggle",
                "state": {"instance": "backlight", "value": true},
                "parameters": {"instance": "backlight", "name": "подсветка"},
            },
        ],
        "properties": [
            {
                "type": "devices.properties.float",
                "retrievable": true,
                "reportable": true,
                "parameters": {
                    "instance": "temperature",
                    "name": "температура",
                    "unit": "unit.temperature.celsius",
                },
                "state": {"percent": null, "status": null, "value": 87},
                "state_changed_at": "2024-01-07T06:26:16Z",
                "last_updated": "2024-01-07T06:26:16Z",
            }
        ],
        "item_type": "device",
        "skill_id": "xxx",
        "room_name": "Кухня",
        "state": "online",
        "created": "2022-10-01T12:09:19Z",
        "parameters": {
            "device_info": {
                "manufacturer": "Polaris",
                "model": "PWK 1725CGLD",
                "hw_version": "",
                "sw_version": "2.18",
            }
        },
    }

    state = update_ha_state(YandexKettle, device)
    assert state.state == "black_tea"
    assert state.attributes == {
        "min_temp": 30,
        "max_temp": 100,
        "operation_list": [
            "on",
            "off",
            "white_tea",
            "green_tea",
            "red_tea",
            "herbal_tea",
            "flower_tea",
            "puerh_tea",
            "oolong_tea",
            "black_tea",
        ],
        "current_temperature": 87,
        "temperature": 65,
        "target_temp_high": null,
        "target_temp_low": null,
        "operation_mode": "black_tea",
        "away_mode": "off",
        "friendly_name": "Чайник",
        "supported_features": (
            WaterHeaterEntityFeature.TARGET_TEMPERATURE
            | WaterHeaterEntityFeature.OPERATION_MODE
            | WaterHeaterEntityFeature.AWAY_MODE
        ),
    }