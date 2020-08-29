function sendMail(contactForm) {
    emailjs.send("gmail", "philanthropist", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
    }).then(
        function (response) {
            console.log("Email Sent!", response);
            swal({
                title: "Your Email was Sent!",
                text: "Thank you for subscribing to Elite Gourmet. \n We will be in touch with you shortly.",
                icon: "success",
                button: "Return to Site",
              });
        },
        function (error) {
            console.log("Email Not Sent...", error);
            swal({
                title: "Ooops!",
                text: "We're sorry, there was an error! \n Please try again.",
                icon: "error",
                button: "Try Again",
              });
        });
    return false;
}