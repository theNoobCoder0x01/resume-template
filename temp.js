const moment = require('moment-timezone');

// Example epoch timestamp (in seconds)
const epochTimestamp = 1721142000; // This represents some date and time

// Define the target time zone
const targetTimeZone = 'America/New_York';

// Convert the epoch timestamp to a moment object in the target time zone
const currentTime = moment.unix(epochTimestamp).tz(targetTimeZone);

// Calculate the GMT offset in seconds for 12 PM in the target time zone
const targetNoon = currentTime.clone().hour(12).minute(0).second(0).millisecond(0);
const gmtOffsetSeconds = targetNoon.utcOffset() * 60;

// Output the GMT offset in seconds
console.log(`GMT offset in seconds: ${gmtOffsetSeconds}`);

// Calculate the previous day's 12 AM, 12 PM, and 11:59:59 PM in the target time zone
const previousDayStart = currentTime.clone().subtract(1, 'day').startOf('day');
const previousDayNoon = previousDayStart.clone().add(12, 'hours');
const previousDayEnd = previousDayStart.clone().endOf('day');

// Calculate the epoch timestamps
const previousDayStartEpoch = previousDayStart.unix();
const previousDayNoonEpoch = previousDayNoon.unix();
const previousDayEndEpoch = previousDayEnd.unix();

// Output the epoch timestamps for 12 AM, 12 PM, and 11:59:59 PM of the previous day in the target time zone
console.log(`Epoch timestamp for previous day's 12 AM: ${previousDayStartEpoch}`);
console.log(`Epoch timestamp for previous day's 12 PM: ${previousDayNoonEpoch}`);
console.log(`Epoch timestamp for previous day's 11:59:59 PM: ${previousDayEndEpoch}`);
