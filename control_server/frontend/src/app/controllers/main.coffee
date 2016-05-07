angular.module('arduinoBattle')
.controller 'MainCtrl', ($scope, $log, CarResource, userService) ->
    $scope.cars = []

    cars = CarResource.query ->
        for car in cars
            $scope.cars.push(car)
            
    userService.getUser()
    $scope.user = userService.username