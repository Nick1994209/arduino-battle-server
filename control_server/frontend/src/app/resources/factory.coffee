angular.module('arduinoBattle')

.factory 'CarResource', ($resource, config) ->
    url = "#{ config.serverAddress }/car/:id/"
    return $resource(url, {}, {create: method:'POST', params:{charge:true}}) # тупо добавил еще 1 метод, старые остались

#.factory 'CarCreate', ($resource, config) ->
#    url = "#{ config.serverAddress }/car/"
#    return $resource(url, {}, {charge: method:'POST', params:{charge:true}})

.factory('UserResource', ['$resource', 'config', ($resource, config) ->
    url = "#{ config.serverAddress }/get_user_data/"
    return $resource(url, {}, {query: {method: 'get', isArray: false}})
])