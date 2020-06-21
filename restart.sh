#!/bin/bash

systemctl restart nginx; systemctl restart ticketapp
systemctl status nginx; systemctl restart ticketapp
