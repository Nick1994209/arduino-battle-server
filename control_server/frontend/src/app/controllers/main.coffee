angular.module('arduinoBattle')
.controller 'MainCtrl', ($scope, $log, CarResource, userService) ->
    $scope.cars = CarResource.query()
    
#    $scope.cars_p = CarResource.query (cars_data)->
#        for car in cars_data
#            $scope.cars.push(car)

    $scope.userData = userService.getUserData()

#    userService.getUsername()
#    $scope.service = userService