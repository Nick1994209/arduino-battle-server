angular.module('arduinoBattle')
.controller 'MainCtrl', ($scope, $log, CarResource, userService) ->
    $scope.cars = []

    cars = CarResource.query ->
        for car in cars
            $scope.cars.push(car)
            
    userService.getUsername()
    $scope.username = userService.username
    console.log $scope