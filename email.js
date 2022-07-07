//list of invalid domains
let invalidDomains = [
  "yahoo.com",
  "gmail.com",
  "outlook.com",
  "google.com",
  "hotmail.com",
  "me.com",
  "icloud.com",
  "aol.com",
  "gmx.com",
  "mac.com",
  "live.com",
  "comcast.com",
  "googlemail.com",
  "msn.com",
  "hotmail.co.uk",
  "yahoo.co.uk",
  "facebook.com",
  "verizon.net",
  "att.net",
  "gmz.com",
  "mail.com",
  "protonmail.com",
];

function validateEmail(event) {
  //Collecting user input and turning it to lower case
  event.preventDefault();
  var email = document.getElementById("email").value;

  if (!email) {
    return console.error("Please enter a valid email");
  }

  const domain = email.toLowerCase().split("@")[1];

  const validRegex =
    /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

  // check standard email input
  if (!email.match(validRegex)) {
    return console.error("Please enter a valid email");
  }

  // check for forbidden domains
  for (let invalidDomain of invalidDomains) {
    if (domain === invalidDomain) {
      return console.error("Please enter a corporate email");
    }
  }

  return console.log("Correct email entered");
}
