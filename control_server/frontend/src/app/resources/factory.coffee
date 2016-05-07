angular.module('arduinoBattle')

.factory 'CarResource', ($resource, config) ->
    url = "#{ config.serverAddress }/car/:id/"
    return $resource(url)

.factory('UserResource', ['$resource', ($resource, config) ->
    url = "#{ config.serverAddress }/get_user/"
    return $resource(url)
])