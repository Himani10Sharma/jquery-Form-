console.log("ok")
$("#myform").validate({
    rules: {
        'username': {
             maxlength:50,
             minlength:1,
            required: true,
        },
            'email': {
            required: true,
            minlength:5,
            maxlength:40,
    },

            'text': {
            required: true,
            minlength:1,
            maxlength:80,
    },

       'password': {
            required: true,
            minlength:4,
            maxlength:8,
    }

},

    messages: {
        "username": {
             required: 'Please enter the username.',
             regex: 'Please enter valid username.',
             maxlength: 'Username  can have at most 50 characters.'
        },

        "email": {
           required: 'Please enter the email.',
           email: 'Please enter valid email address.',

           maxlength: 'email length is upto 40 characters.',
           minlength:'email length can not be too short',
},

        "text": {
           required: 'Please enter some text',

           maxlength: 'text length is upto 80 characters.',
           minlength:'text length can not be too short',
},
         "password": {
           required: 'Please enter valid password',

           maxlength: 'password length is upto 8 characters.',
           minlength:'password length can not be too short',
}
}
});
