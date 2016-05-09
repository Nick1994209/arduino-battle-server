angular.module('arduinoBattle')

.factory 'CarResource', ($resource, config) ->
    url = "#{ config.serverAddress }/car/:id/"
    return $resource(url, {}, {create: {method:'POST', params:{}}}) # тупо добавил еще 1 метод, старые остались


.factory('UserResource', ['$resource', 'config', ($resource, config) ->
    url = "#{ config.serverAddress }/get_user_data/"
    return $resource(url, {}, {query: {method: 'get', isArray: false}})
])