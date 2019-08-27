
// Get URL and query parameters
let url = new URL(window.location.href);
let username = url.searchParams.get("username");
let delay = url.searchParams.get("delay");

// Log current user and delay
console.log("User: " + username);
console.log("Delay: " + delay);

// Refresh page every 'delay' milliseconds and send log
setInterval(
  () => {
    location.reload(true);
    console.log("Reloading");
  },
  delay
);
