angular.module('arduinoBattle')

.service('userService', ['UserResource', (UserResource) -> 
    self = this
    self.username = undefined 
    self.getUserData = () ->
        UserResource.query(
          ((data) ->
              self.username = data['username']
          ),
          ((errors) ->
              console.log(errors)
          )
        )
    return undefined 
])

.service('carCreateService', ()->
#    this.createCar = (carData) ->
#        CarCreateService.post()
    a = 32
)