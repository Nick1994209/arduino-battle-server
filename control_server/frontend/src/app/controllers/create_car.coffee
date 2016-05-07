angular.module('arduinoBattle')

.controller('CreateCarCtrl', ($scope, CarResource, userService)->
    userService.getUserData()
    $scope.userService = userService

    $scope.addCar = ()->
        console.log $scope.address, $scope.name
        if $scope.address and $scope.name and $scope.userService.username
            carData = {addres: $scope.address, name:$scope.name, username: $scope.userService.username}
            $scope.errors = undefined 
            CarResource.create(carData)
        else
            $scope.errors = 'Что то не так'

)
