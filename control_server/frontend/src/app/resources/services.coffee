angular.module('arduinoBattle')

.service('userService', ['UserResource', (UserResource) -> 
    self = this
    self.username = undefined 
    self.idUser = undefined 
    self.getUserData = () ->
        UserResource.query(
          ((data) ->
              self.username = data['username']
              self.idUser = data['id']
          ),
          ((errors) ->
              console.log(errors)
          )
        )
    return undefined 
])