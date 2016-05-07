angular.module('arduinoBattle')

.service('userService', ['UserResource', (UserResource) -> 
    self = this
    self.username = undefined 
    this.getUsername = () ->
        console.log(1232132132133123123)
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