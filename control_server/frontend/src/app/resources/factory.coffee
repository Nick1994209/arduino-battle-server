angular.module('arduinoBattle')

.factory 'CarResource', ($resource, config) ->
    url = "#{ config.serverAddress }/car/:id/"
    return $resource(url)

.factory('UserResource', ['$resource', 'config', ($resource, config) ->
    url = "#{ config.serverAddress }/get_user/"
    return $resource(url, {}, {query: {method: 'get', isArray: false}})
])