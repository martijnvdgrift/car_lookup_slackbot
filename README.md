# Slack bot: Car Lookup

https://xebia.slack.com/apps/manage

## Components:

- Open data: [RWD gekentekende voertuigen](https://opendata.rdw.nl/Voertuigen/Open-Data-RDW-Gekentekende_voertuigen/m9d7-ebf2)
- Github project: [Open Automated LicencePlate Recogniser](https://github.com/openalpr/openalpr)

    $ docker build -t bija/car_lookup .
    $ docker run -e DEBUG="True" -e ACTIVE_TOKEN=xyz -v $(pwd):/data:ro -v /dev/null:/dev/raw1394 -p 5000:5000 bija/car_lookup

## Testing locally

- [http://localhost:5000/test?kenteken=28-ZTP-6](http://localhost:5000/test?kenteken=28-ZTP-6)
- [http://localhost:5000/test?file=someimage.jpg](http://localhost:5000/test?file=someimage.jpg)


### TODO's:

- Use a single command `/kenteken` and not also `/my_car` and use an english name, I like: `/car` simple and short!