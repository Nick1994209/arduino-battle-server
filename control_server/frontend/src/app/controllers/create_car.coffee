angular.module('arduinoBattle')

.controller('CreateCarCtrl', ($scope, CarResource, userService)->
    userService.getUserData()
    $scope.userService = userService

    $scope.addCar = ()->
        console.log $scope.address, $scope.name

        if $scope.address and $scope.name and $scope.userService.username
            carData = {address: $scope.address, name:$scope.name}#, user: $scope.userService.username}
            $scope.errors = undefined
            CarResource.save(carData, (created_data)->
                $scope.created = "Машинка #{ $scope.name } была добавлена пользователю"
                console.log(created_data)
                # TODO сделать редирект на машинку
            ,()->
                $scope.created = undefined 
                $scope.errors = "Машинка '#{ $scope.name }' уже существует или адрес введен неверно '#{ $scope.address }'  пример: '127.0.0.1'"
            )
        else
            $scope.errors = 'Не заполнены поля (скорее всего)'

)
