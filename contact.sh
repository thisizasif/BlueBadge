#!/bin/bash

# Variables to track subscription and social media join status
SUBSCRIBED=false
JOINED_TELEGRAM=false
JOINED_WHATSAPP=false
JOINED_INSTAGRAM=false
JOINED_TWITTER=false

TELEGRAM_CHANNEL="t.me/YOUR_TELEGRAM_CHANNEL"
WHATSAPP_GROUP="chat.whatsapp.com/YOUR_WHATSAPP_GROUP"
INSTAGRAM_PROFILE="instagram.com/YOUR_INSTAGRAM_PROFILE"
TWITTER_PROFILE="twitter.com/YOUR_TWITTER_PROFILE"

check_subscription() {
    read -p "Have you subscribed to our YouTube channel? (y/n): " youtube_response

    case $youtube_response in
        [Yy])
            echo "Thank you for subscribing to our YouTube channel!"
            SUBSCRIBED=true

            read -p "Would you like to join our Telegram channel? (y/n): " telegram_response

            case $telegram_response in
                [Yy])
                    echo "Great! Join our Telegram channel: $TELEGRAM_CHANNEL"
                    JOINED_TELEGRAM=true
                    ;;
                [Nn])
                    echo "You can join our Telegram channel anytime. Thank you!"
                    ;;
                *)
                    echo "Invalid response. Please enter 'y' or 'n'."
                    ;;
            esac

            read -p "Would you like to join our WhatsApp group? (y/n): " whatsapp_response

            case $whatsapp_response in
                [Yy])
                    echo "Awesome! Join our WhatsApp group: $WHATSAPP_GROUP"
                    JOINED_WHATSAPP=true
                    ;;
                [Nn])
                    echo "You can join our WhatsApp group anytime. Thank you!"
                    ;;
                *)
                    echo "Invalid response. Please enter 'y' or 'n'."
                    ;;
            esac

            read -p "Would you like to follow us on Instagram? (y/n): " instagram_response

            case $instagram_response in
                [Yy])
                    echo "Fantastic! Follow us on Instagram: $INSTAGRAM_PROFILE"
                    JOINED_INSTAGRAM=true
                    ;;
                [Nn])
                    echo "You can follow us on Instagram anytime. Thank you!"
                    ;;
                *)
                    echo "Invalid response. Please enter 'y' or 'n'."
                    ;;
            esac

            read -p "Would you like to follow us on Twitter? (y/n): " twitter_response

            case $twitter_response in
                [Yy])
                    echo "Excellent! Follow us on Twitter: $TWITTER_PROFILE"
                    JOINED_TWITTER=true
                    ;;
                [Nn])
                    echo "You can follow us on Twitter anytime. Thank you!"
                    ;;
                *)
                    echo "Invalid response. Please enter 'y' or 'n'."
                    ;;
            esac
            ;;
        [Nn])
            echo "Please subscribe to our YouTube channel: https://www.youtube.com/channel/YOUR_CHANNEL_ID"
            exit 0
            ;;
        *)
            echo "Invalid response. Please enter 'y' or 'n'."
            check_subscription
            ;;
    esac
}

if $SUBSCRIBED; then
    echo "You are already subscribed. Thank you!"
else
    check_subscription
fi

if $JOINED_TELEGRAM; then
    echo "You have already joined our Telegram channel. Thank you!"
fi

if $JOINED_WHATSAPP; then
    echo "You have already joined our WhatsApp group. Thank you!"
fi

if $JOINED_INSTAGRAM; then
    echo "You have already followed us on Instagram. Thank you!"
fi

if $JOINED_TWITTER; then
    echo "You have already followed us on Twitter. Thank you!"
fi
