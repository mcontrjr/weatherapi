# coding: utf-8

"""
    Weather API

     # Introduction  WeatherAPI.com provides access to weather and geo data via a JSON/XML restful API. It allows developers to create desktop, web and mobile applications using this data very easy.      We provide following data through our API:      - Real-time weather  - 14 day weather forecast  - Astronomy  - Time zone  - Location data  - Search or Autocomplete API  - NEW: Historical weather  - NEW: Future Weather (Upto 300 days ahead)  - Weather Alerts  - Air Quality Data    # Getting Started     You need to [signup](https://www.weatherapi.com/signup.aspx) and then you can find your API key under [your account](https://www.weatherapi.com/login.aspx), and start using API right away!      We have [code libraries](https://www.weatherapi.com/docs/code-libraries.aspx) for different programming languages like PHP, .net, JAVA, etc.  If you find any features missing or have any suggestions, please [contact us](https://www.weatherapi.com/contact.aspx).      # Authentication     API access to the data is protected by an API key. If at anytime, you find the API key has become vulnerable, please regenerate the key using Regenerate button next to the API key.  Authentication to the WeatherAPI.com API is provided by passing your API key as request parameter through an API .        ##  key parameter   key=YOUR_API_KEY   # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse2001(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'location': 'Location',
        'current': 'Current',
        'forecast': 'Forecast',
        'alerts': 'Alerts'
    }

    attribute_map = {
        'location': 'location',
        'current': 'current',
        'forecast': 'forecast',
        'alerts': 'alerts'
    }

    def __init__(self, location=None, current=None, forecast=None, alerts=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger"""  # noqa: E501
        self._location = None
        self._current = None
        self._forecast = None
        self._alerts = None
        self.discriminator = None
        if location is not None:
            self.location = location
        if current is not None:
            self.current = current
        if forecast is not None:
            self.forecast = forecast
        if alerts is not None:
            self.alerts = alerts

    @property
    def location(self):
        """Gets the location of this InlineResponse2001.  # noqa: E501


        :return: The location of this InlineResponse2001.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this InlineResponse2001.


        :param location: The location of this InlineResponse2001.  # noqa: E501
        :type: Location
        """

        self._location = location

    @property
    def current(self):
        """Gets the current of this InlineResponse2001.  # noqa: E501


        :return: The current of this InlineResponse2001.  # noqa: E501
        :rtype: Current
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this InlineResponse2001.


        :param current: The current of this InlineResponse2001.  # noqa: E501
        :type: Current
        """

        self._current = current

    @property
    def forecast(self):
        """Gets the forecast of this InlineResponse2001.  # noqa: E501


        :return: The forecast of this InlineResponse2001.  # noqa: E501
        :rtype: Forecast
        """
        return self._forecast

    @forecast.setter
    def forecast(self, forecast):
        """Sets the forecast of this InlineResponse2001.


        :param forecast: The forecast of this InlineResponse2001.  # noqa: E501
        :type: Forecast
        """

        self._forecast = forecast

    @property
    def alerts(self):
        """Gets the alerts of this InlineResponse2001.  # noqa: E501


        :return: The alerts of this InlineResponse2001.  # noqa: E501
        :rtype: Alerts
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this InlineResponse2001.


        :param alerts: The alerts of this InlineResponse2001.  # noqa: E501
        :type: Alerts
        """

        self._alerts = alerts

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse2001, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2001):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other