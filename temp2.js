const moment = require('moment-timezone');

// Example epoch timestamp (in seconds)
const epochTimestamp = 1721197800; // This represents some date and time

// Convert the epoch timestamp to a moment object in UTC
const currentTime = moment.unix(epochTimestamp);

// Get all time zones
const timeZones = moment.tz.names();
const matchingTimeZones = [];

// Check each time zone
timeZones.forEach((timeZone) => {
    const localTime = currentTime.tz(timeZone);
    if (localTime.hour() === 12 && localTime.minute() === 0) {
        matchingTimeZones.push(timeZone);
    }
});

// Output the time zones where it is 12 PM at the given epoch timestamp
console.log(`Time zones where it is 12 PM:`, matchingTimeZones);
