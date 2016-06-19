angular.module('arduinoBattle')

.controller('CreateCarCtrl', ($scope, CarResource, userService)->
    userService.getUserData()
    $scope.userService = userService

    $scope.addCar = ()->
        console.log $scope.address, $scope.name

        if $scope.address and $scope.name and $scope.userService.idUser
            carData = {address: $scope.address, name:$scope.name, user: $scope.userService.idUser}
            $scope.errors = undefined
            CarResource.save(carData, ()->
                $scope.created = "Машинка #{ $scope.name } была добавлена пользователю"
            ,()->
                $scope.created = undefined 
                $scope.errors = "Машинка #{ $scope.address } или #{ $scope.name } уже существует"
            )
        else
            $scope.errors = 'Что то не так'

)
