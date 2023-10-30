from client.web.base_web_client import BaseWebClient


class VehiclesCommandClient(BaseWebClient):

    def actuate_trunk(self, id, which_trunk):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/actuate_trunk",
            params=None,
            json={"id": id, "which_trunk": which_trunk},
        )

    def adjust_volume(self, id, volume):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/adjust_volume",
            params=None,
            json={"id": id, "volume": volume},
        )

    def auto_conditioning_start(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/auto_conditioning_start",
            params=None,
            json={"id": id},
        )

    def auto_conditioning_stop(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/auto_conditioning_stop",
            params=None,
            json={"id": id},
        )

    def cancel_software_update(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/cancel_software_update",
            params=None,
            json={"id": id},
        )

    def charge_max_range(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/charge_max_range",
            params=None,
            json={"id": id},
        )

    def charge_port_door_close(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/charge_port_door_close",
            params=None,
            json={"id": id},
        )

    def charge_port_door_open(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/charge_port_door_open",
            params=None,
            json={"id": id},
        )

    def charge_standard(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/charge_standard",
            params=None,
            json={"id": id},
        )

    def charge_start(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/charge_start",
            params=None,
            json={"id": id},
        )

    def charge_stop(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/charge_stop",
            params=None,
            json={"id": id},
        )

    def door_lock(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/door_lock",
            params=None,
            json={"id": id},
        )

    def door_unlock(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/door_unlock",
            params=None,
            json={"id": id},
        )

    def erase_user_data(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/erase_user_data",
            params=None,
            json={"id": id},
        )

    def flash_lights(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/flash_lights",
            params=None,
            json={"id": id},
        )

    def guest_mode(self, id, enable):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/guest_mode",
            params=None,
            json={"id": id, "enable": enable},
        )

    def honk_horn(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/honk_horn",
            params=None,
            json={"id": id},
        )

    def media_next_fav(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/media_next_fav",
            params=None,
            json={"id": id},
        )

    def media_next_track(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/media_next_track",
            params=None,
            json={"id": id},
        )

    def media_prev_fav(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/media_prev_fav",
            params=None,
            json={"id": id},
        )

    def media_prev_track(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/media_prev_track",
            params=None,
            json={"id": id},
        )

    def media_toggle_playback(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/media_toggle_playback",
            params=None,
            json={"id": id},
        )

    def media_volume_down(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/media_volume_down",
            params=None,
            json={"id": id},
        )

    def navigation_gps_request(self, id, lat, lon, order):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/navigation_gps_request",
            params=None,
            json={"id": id, "lat": lat, "lon": lon, "order": order},
        )

    def navigation_request(self, id, type, value, locale, timestamp_ms):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/navigation_request",
            params=None,
            json={"id": id, "type": type, "value": value,
                  "locale": locale, "timestamp_ms": timestamp_ms},
        )

    def navigation_sc_request(self, id, order):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/navigation_sc_request",
            params=None,
            json={"id": id, "order": order},
        )

    def remote_auto_seat_climate_request(self, id, auto_seat_position, auto_climate_on):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/remote_auto_seat_climate_request",
            params=None,
            json={"id": id, "auto_seat_position": auto_seat_position,
                  "auto_climate_on": auto_climate_on},
        )

    def remote_auto_steering_wheel_heat_climate_request(self, id, on):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/remote_auto_steering_wheel_heat_climate_request",
            params=None,
            json={"id": id, "on": on},
        )

    def remote_boombox(self, id, sound):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/remote_boombox",
            params=None,
            json={"id": id, "sound": sound},
        )

    def remote_seat_cooler_request(self, id, seat_position, seat_cooler_level):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/remote_seat_cooler_request",
            params=None,
            json={"id": id, "seat_position": seat_position,
                  "seat_cooler_level": seat_cooler_level},
        )

    def remote_seat_heater_request(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/remote_seat_heater_request",
            params=None,
            json={"id": id},
        )

    def remote_start_drive(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/remote_start_drive",
            params=None,
            json={"id": id},
        )

    def remote_steering_wheel_heat_level_request(self, id, level):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/remote_steering_wheel_heat_level_request",
            params=None,
            json={"id": id, "level": level},
        )

    def remote_steering_wheel_heater_request(self, id, on):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/remote_steering_wheel_heater_request",
            params=None,
            json={"id": id, "on": on},
        )

    def reset_pin_to_drive_pin(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/reset_pin_to_drive_pin",
            params=None,
            json={"id": id},
        )

    def reset_valet_pin(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/reset_valet_pin",
            params=None,
            json={"id": id},
        )

    def schedule_software_update(self, id, offset_sec):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/schedule_software_update",
            params=None,
            json={"id": id, "offset_sec": offset_sec},
        )

    def set_bioweapon_mode(self, id, on, manual_override):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/set_bioweapon_mode",
            params=None,
            json={"id": id, "on": on, "manual_override": manual_override},
        )

    def set_cabin_overheat_protection(self, id, on, fan_only):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/set_cabin_overheat_protection",
            params=None,
            json={"id": id, "on": on, "fan_only": fan_only},
        )

    def set_charge_limit(self, id, percent):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/set_charge_limit",
            params=None,
            json={"id": id, "percent": percent},
        )

    def set_charging_amps(self, id, charging_amps):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/set_charging_amps",
            params=None,
            json={"id": id, "charging_amps": charging_amps},
        )

    def set_climate_keeper_mode(self, id, climate_keeper_mode):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/set_climate_keeper_mode",
            params=None,
            json={"id": id, "climate_keeper_mode": climate_keeper_mode},
        )

    def set_cop_temp(self, id, cop_temp):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/set_cop_temp",
            params=None,
            json={"id": id, "cop_temp": cop_temp},
        )

    def set_managed_charge_current_request(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/set_managed_charge_current_request",
            params=None,
            json={"id": id},
        )

    def set_managed_charger_location(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/set_managed_charger_location",
            params=None,
            json={"id": id},
        )

    def set_managed_scheduled_charging_time(self, id):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/set_managed_scheduled_charging_time",
            params=None,
            json={"id": id},
        )

    def set_pin_to_drive(self, id, on, password):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/set_pin_to_drive",
            params=None,
            json={"id": id, "on": on, "password": password},
        )

    def set_preconditioning_max(self, id, on, manual_override):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/set_preconditioning_max",
            params=None,
            json={"id": id, "on": on, "manual_override": manual_override},
        )

    def set_scheduled_charging(self, id, enable, time):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/set_scheduled_charging",
            params=None,
            json={"id": id, "enable": enable, "time": time},
        )

    def set_scheduled_departure(self, id, enable, time):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/set_scheduled_departure",
            params=None,
            json={"id": id, "enable": enable, "time": time},
        )

    def set_sentry_mode(self, id, on):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/set_sentry_mode",
            params=None,
            json={"id": id, "on": on},
        )

    def set_temps(self, id, driver_temp, passenger_temp):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/set_temps",
            params=None,
            json={"id": id, "driver_temp": driver_temp,
                  "passenger_temp": passenger_temp},
        )

    def set_valet_mode(self, id, on, password):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/set_valet_mode",
            params=None,
            json={"id": id, "on": on, "password": password},
        )

    def set_vehicle_name(self, id, vehicle_name):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/set_vehicle_name",
            params=None,
            json={"id": id, "vehicle_name": vehicle_name},
        )

    def speed_limit_activate(self, id, pin):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/speed_limit_activate",
            params=None,
            json={"id": id, "pin": pin},
        )

    def speed_limit_clear_pin(self, id, pin):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/speed_limit_clear_pin",
            params=None,
            json={"id": id, "pin": pin},
        )

    def speed_limit_deactivate(self, id, pin):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/speed_limit_deactivate",
            params=None,
            json={"id": id, "pin": pin},
        )

    def speed_limit_set_limit(self, id, limit_mph):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/speed_limit_set_limit",
            params=None,
            json={"id": id, "limit_mph": limit_mph},
        )

    def sun_roof_control(self, id, state):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/sun_roof_control",
            params=None,
            json={"id": id, "state": state},
        )

    def take_drivenote(self, id, note):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/take_drivenote",
            params=None,
            json={"id": id, "note": note},
        )

    def trigger_homelink(self, id, lat, lon, token):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/trigger_homelink",
            params=None,
            json={"id": id, "lat": lat, "lon": lon, "token": token},
        )

    def update_calendar_entries(self, id, calendar_data):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/update_calendar_entries",
            params=None,
            json={"id": id, "calendar_data": calendar_data},
        )

    def window_control(self, id, lat, lon, command):
        return self.httpPost(
            f"/api/1/vehicles/{id}/command/window_control",
            params=None,
            json={"id": id, "lat": lat, "lon": lon, "command": command},
        )
