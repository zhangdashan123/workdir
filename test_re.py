# coding:utf-8
import re

str_data = """
infosite.offersData= {
                "offers": [
                    {
                    "nightlyRates": [],
                    "hotelID": "33204043",
                    "roomTypeCode": "213605639",
                    "ratePlanCode": "244100588",
                    "piid": "LPASTESTPIID_V3",
                    "roomName": "",
                    "activityID": "1c4bacb5-b193-4719-979c-adf5ef5414a3",
                    "numberOfNights": 1,
                    "insideWindowPenaltyNightCount": 1,
                    "insideWindowPenaltyPercentage": 0,
                    "outsideWindowPenaltyNightCount": 0,
                    "outsideWindowPenaltyPercentage": 0,
                    "cancellationWindowDate": "9月19日星期四",
                    "cancellationWindowTime": "18:00",
                    "cancellationTimeZoneName": "中国标准时间",
                    "feePenalty": {
                        "amount": 0.00,
                        "currency": "USD",
                        "currencyCode": "USD",
                        "negative": false,
                        "double": 0.0
                    },
                    "insideFeePenalty": {
                        "amount": 0.00,
                        "currency": "USD",
                        "currencyCode": "USD",
                        "negative": false,
                        "double": 0.0
                    },
                    "checkInDate": "2019/09/20",
                    "checkOutDate": "2019/09/21",
                    "offerType": "5",
                    "maxGuests": 0,
                    "maxAdults": 0,
                    "maxChildren": 0,
                    "showETPTooltip": true,
                    "minGuestAge": 0,
                    "numberOfRoomsLeft": 3,
                    "showRoomsLeftMessage": true,
                    "price": {
                        "available": true,
                        "displayPrice": "CNY439",
                        "chargedDisplayPrice": "US$62",
                        "crossOutPrice": null,
                        "totalPriceWithoutMandatoryFee": 0.0,
                        "perPersonTotalPrice": 0.0,
                        "perNightTotalPrice": 0.0,
                        "formattedDiscountAmount": null,
                        "formattedTotalLoyaltyPoints": null,
                        "percentageDiscount": 0,
                        "discountAmount": 0,
                        "totalPrice": 439.11,
                        "displayViewTotalPrice": false,
                        "oneNightStay": false,
                        "expediaPointsBranded": "Expedia+ 积分",
                        "displayTotalPriceWithTaxesAndFees": "CNY512",
                        "chargedDisplayTotalPriceWithTaxesAndFees": "US$72",
                        "isPackageSavingsSignificant": false,
                        "displayTotalPrice": "CNY439",
                        "priceObject": {
                            "amount": 439.11,
                            "currency": "CNY",
                            "currencyCode": "CNY",
                            "negative": false,
                            "double": 439.11
                        },
                        "packageSavingsSignificant": false,
                        "price": 439.11,
                        "unformattedCrossOutPrice": 0.0,
                        "unformattedTotalPrice": "439.11"
                    },
                    "totalPriceWithTaxesAndFees": {
                        "amount": 512.00,
                        "currency": "CNY",
                        "currencyCode": "CNY",
                        "negative": false,
                        "double": 512.0
                    },
                    "currencyPosa": "CNY",
                    "currencyPosu": "CNY",
                    "billingCurrencyCode": "USD",
                    "quotedRate": 439.11,
                    "resortFee": null,
                    "taxableServiceFee": null,
                    "taxesAndFeesNotIncludedInPrice": {
                        "amount": 72.89,
                        "currency": "CNY",
                        "currencyCode": "CNY",
                        "negative": false,
                        "double": 72.89
                    },
                    "totalWithCityTax": {
                        "amount": 584.89,
                        "currency": "CNY",
                        "currencyCode": "CNY",
                        "negative": false,
                        "double": 584.89
                    },
                    "drrId": 0,
                    "showMemberDiscountBadge": true,
                    "drrMessage": "",
                    "drrExpirationSecs": 1884419416,
                    "drrExpirationDate": "2079/6/6",
                    "tonightOnlyDRRSaveValue": "",
                    "valueAdd": {},
                    "loyaltyEarnPoints": null,
                    "earnRewardsForGPS": null,
                    "earnRewardsText": null,
                    "drrMessageForGPSEnabled": false,
                    "earnRewardsGPSLogoEnabled": false,
                    "exclusiveOfferMsg": null,
                    "loyaltyEarnPrice": null,
                    "loyaltyBurnedPrice": null,
                    "totalLoyaltyBurnedPriceWithTaxesAndFees": null,
                    "loyaltyCrossOutPrice": null,
                    "totalLoyaltyCrossOutPriceWithTaxesAndFees": null,
                    "includedFees": {
                        "fees": [],
                        "displayTotal": null,
                        "totalAmount": 0,
                        "showMandatoryFee": false,
                        "usePOSuCurrency": false
                    },
                    "excludedFees": {
                        "fees": [],
                        "displayTotal": null,
                        "totalAmount": 0,
                        "showMandatoryFee": false,
                        "usePOSuCurrency": false
                    },
                    "homeAwayRDD": null,
                    "homeAwayRDDIncluded": false,
                    "amenities": {},
                    "inventoryProviderID": 24,
                    "loyaltyBaseEarnPrice": null,
                    "loyaltyBonusEarnPrice": null,
                    "earnModifierOperation": null,
                    "earnModifierValue": null,
                    "eligibleForTaapDeferredPayment": false,
                    "taapDeferredPaymentDateWindow": null,
                    "airAttachDiscountPercentage": null,
                    "conversionNeeded": true,
                    "displayNightlyRateDisclaimer": false,
                    "travelerServiceFee": null,
                    "travelerAndTaxableServiceFee": null,
                    "cartId": null,
                    "bundleId": null,
                    "containsL26Taxes": false,
                    "shpmDiscountModel": null,
                    "roomOccupants": "rm1=a2",
                    "multiItem": false,
                    "multiCurrencyEnabled": true,
                    "payLater": true,
                    "nonRefundableInsideWindow": true,
                    "nonRefundableOutsideWindow": false,
                    "paymentChoiceAvailable": true,
                    "priceModified": false,
                    "artificiallyFencedRate": false,
                    "bookable": true,
                    "udp": true,
                    "multiCurrencyBillingEnabled": true,
                    "drrpresent": false,
                    "tonightOnlyDRRPresent": false,
                    "promoMsgEnabledHIS": false,
                    "memberExclusiveDRRPresent": false,
                    "memberExclusiveDRRAvailable": false,
                    "mobileExclusive": false,
                    "removeDrrTooltip": false,
                    "showTdEarnMessage": false,
                    "modHisMeatStickerEnabled": false,
                    "showCancellationMsg_1": false,
                    "showCancellationMsg_1_v2": false,
                    "showCancellationMsg_2": false,
                    "showCancellationMsg_2_v2": false,
                    "showCancellationMsg_3": false,
                    "showCancellationMsg_3_v2": false,
                    "showCancellationMsg_4": false,
                    "showCancellationMsg_4_v2": false,
                    "showCancellationMsg_5": false,
                    "showCancellationMsg_5_v2": false,
                    "showCancellationMsg_6": false,
                    "showCancellationMsg_6_v2": false,
                    "showCancellationMsg_7": false,
                    "showCancellationMsg_7_v2": true,
                    "showCancellationMsg_8": false,
                    "showCancellationMsg_8_v2": false,
                    "showCancellationMsg_9": false,
                    "showCancellationMsg_9_v2": false,
                    "showCancellationMsg_10": false,
                    "showCancellationMsg_10_v2": false,
                    "showCancellationMsg_11": false,
                    "showCancellationMsg_11_v2": false,
                    "showCancellationMsg_12": false,
                    "showCancellationMsg_13": false,
                    "outsideCancelPolicyMsgKey": null,
                    "insideCancelPolicyMsgKey": "cancellation.inside.NightFullPenalty.b",
                    "agencyReserveNowPayLater": false,
                    "showCancelPolicy": true,
                    "insideFeePenaltyText": "US$0.00",
                    "outsideFeePenaltyText": "US$0.00",
                    "showNightlyRates": false,
                    "drrExpirationSecsText": "1884419416",
                    "drrExpiration_1": false,
                    "drrExpiration_2": false,
                    "drrExpiration_3": false,
                    "drrExpiration_4": true,
                    "airAttach": false,
                    "outsideWindowPrice": false,
                    "insideWindowPrice": false,
                    "showETPDepositChoice": false,
                    "drrDiscountPercentageBased": false,
                    "hasValueAdd": false,
                    "validDRRForExp15881": false,
                    "dealOfTheDayDRRPresent": false,
                    "thirdPartyInventoryProvider": false,
                    "displayMultiSourceToolTip": false,
                    "refundable": true,
                    "isDisplayHPG": true,
                    "loyaltyPointsEnabled": false,
                    "freeOnlineCancellation": false,
                    "mrp": false
                },
                    {
                    "nightlyRates": [],
                    "hotelID": "33204043",
                    "roomTypeCode": "213605639",
                    "ratePlanCode": "244100588",
                    "piid": "LPASTESTPIID_V3",
                    "roomName": "",
                    "activityID": "1c4bacb5-b193-4719-979c-adf5ef5414a3",
                    "numberOfNights": 1,
                    "insideWindowPenaltyNightCount": 1,
                    "insideWindowPenaltyPercentage": 0,
                    "outsideWindowPenaltyNightCount": 0,
                    "outsideWindowPenaltyPercentage": 0,
                    "cancellationWindowDate": "9月19日星期四",
                    "cancellationWindowTime": "18:00",
                    "cancellationTimeZoneName": "中国标准时间",
                    "feePenalty": {
                        "amount": 0.00,
                        "currency": "USD",
                        "currencyCode": "USD",
                        "negative": false,
                        "double": 0.0
                    },
                    "insideFeePenalty": {
                        "amount": 0.00,
                        "currency": "USD",
                        "currencyCode": "USD",
                        "negative": false,
                        "double": 0.0
                    },
                    "checkInDate": "2019/09/20",
                    "checkOutDate": "2019/09/21",
                    "offerType": "1",
                    "maxGuests": 0,
                    "maxAdults": 0,
                    "maxChildren": 0,
                    "showETPTooltip": true,
                    "minGuestAge": 0,
                    "numberOfRoomsLeft": 3,
                    "showRoomsLeftMessage": true,
                    "price": {
                        "available": true,
                        "displayPrice": "CNY439",
                        "chargedDisplayPrice": "US$62",
                        "crossOutPrice": null,
                        "totalPriceWithoutMandatoryFee": 0.0,
                        "perPersonTotalPrice": 0.0,
                        "perNightTotalPrice": 0.0,
                        "formattedDiscountAmount": null,
                        "formattedTotalLoyaltyPoints": null,
                        "percentageDiscount": 0,
                        "discountAmount": 0,
                        "totalPrice": 439.12,
                        "displayViewTotalPrice": false,
                        "oneNightStay": false,
                        "expediaPointsBranded": "Expedia+ 积分",
                        "displayTotalPriceWithTaxesAndFees": "CNY512",
                        "chargedDisplayTotalPriceWithTaxesAndFees": "US$72",
                        "isPackageSavingsSignificant": false,
                        "displayTotalPrice": "CNY439",
                        "priceObject": {
                            "amount": 439.12,
                            "currency": "CNY",
                            "currencyCode": "CNY",
                            "negative": false,
                            "double": 439.12
                        },
                        "packageSavingsSignificant": false,
                        "price": 439.12,
                        "unformattedCrossOutPrice": 0.0,
                        "unformattedTotalPrice": "439.12"
                    },
                    "totalPriceWithTaxesAndFees": {
                        "amount": 512.03,
                        "currency": "CNY",
                        "currencyCode": "CNY",
                        "negative": false,
                        "double": 512.03
                    },
                    "currencyPosa": "CNY",
                    "currencyPosu": "CNY",
                    "billingCurrencyCode": "USD",
                    "quotedRate": 439.12,
                    "resortFee": null,
                    "taxableServiceFee": null,
                    "taxesAndFeesNotIncludedInPrice": {
                        "amount": 72.91,
                        "currency": "CNY",
                        "currencyCode": "CNY",
                        "negative": false,
                        "double": 72.91
                    },
                    "totalWithCityTax": {
                        "amount": 584.94,
                        "currency": "CNY",
                        "currencyCode": "CNY",
                        "negative": false,
                        "double": 584.94
                    },
                    "drrId": 0,
                    "showMemberDiscountBadge": true,
                    "drrMessage": "",
                    "drrExpirationSecs": 1884419416,
                    "drrExpirationDate": "2079/6/6",
                    "tonightOnlyDRRSaveValue": "",
                    "valueAdd": {},
                    "loyaltyEarnPoints": null,
                    "earnRewardsForGPS": null,
                    "earnRewardsText": null,
                    "drrMessageForGPSEnabled": false,
                    "earnRewardsGPSLogoEnabled": false,
                    "exclusiveOfferMsg": null,
                    "loyaltyEarnPrice": null,
                    "loyaltyBurnedPrice": null,
                    "totalLoyaltyBurnedPriceWithTaxesAndFees": null,
                    "loyaltyCrossOutPrice": null,
                    "totalLoyaltyCrossOutPriceWithTaxesAndFees": null,
                    "includedFees": {
                        "fees": [],
                        "displayTotal": null,
                        "totalAmount": 0,
                        "showMandatoryFee": false,
                        "usePOSuCurrency": false
                    },
                    "excludedFees": {
                        "fees": [],
                        "displayTotal": null,
                        "totalAmount": 0,
                        "showMandatoryFee": false,
                        "usePOSuCurrency": false
                    },
                    "homeAwayRDD": null,
                    "homeAwayRDDIncluded": false,
                    "amenities": {},
                    "inventoryProviderID": 24,
                    "loyaltyBaseEarnPrice": null,
                    "loyaltyBonusEarnPrice": null,
                    "earnModifierOperation": null,
                    "earnModifierValue": null,
                    "eligibleForTaapDeferredPayment": false,
                    "taapDeferredPaymentDateWindow": null,
                    "airAttachDiscountPercentage": null,
                    "conversionNeeded": true,
                    "displayNightlyRateDisclaimer": false,
                    "travelerServiceFee": null,
                    "travelerAndTaxableServiceFee": null,
                    "cartId": null,
                    "bundleId": null,
                    "containsL26Taxes": false,
                    "shpmDiscountModel": null,
                    "roomOccupants": "rm1=a2",
                    "multiItem": false,
                    "multiCurrencyEnabled": true,
                    "payLater": false,
                    "nonRefundableInsideWindow": true,
                    "nonRefundableOutsideWindow": false,
                    "paymentChoiceAvailable": true,
                    "priceModified": false,
                    "artificiallyFencedRate": false,
                    "bookable": true,
                    "udp": true,
                    "multiCurrencyBillingEnabled": true,
                    "drrpresent": false,
                    "tonightOnlyDRRPresent": false,
                    "promoMsgEnabledHIS": false,
                    "memberExclusiveDRRPresent": false,
                    "memberExclusiveDRRAvailable": false,
                    "mobileExclusive": false,
                    "removeDrrTooltip": false,
                    "showTdEarnMessage": false,
                    "modHisMeatStickerEnabled": false,
                    "showCancellationMsg_1": false,
                    "showCancellationMsg_1_v2": false,
                    "showCancellationMsg_2": false,
                    "showCancellationMsg_2_v2": false,
                    "showCancellationMsg_3": false,
                    "showCancellationMsg_3_v2": false,
                    "showCancellationMsg_4": false,
                    "showCancellationMsg_4_v2": false,
                    "showCancellationMsg_5": false,
                    "showCancellationMsg_5_v2": false,
                    "showCancellationMsg_6": false,
                    "showCancellationMsg_6_v2": false,
                    "showCancellationMsg_7": false,
                    "showCancellationMsg_7_v2": true,
                    "showCancellationMsg_8": false,
                    "showCancellationMsg_8_v2": false,
                    "showCancellationMsg_9": false,
                    "showCancellationMsg_9_v2": false,
                    "showCancellationMsg_10": false,
                    "showCancellationMsg_10_v2": false,
                    "showCancellationMsg_11": false,
                    "showCancellationMsg_11_v2": false,
                    "showCancellationMsg_12": false,
                    "showCancellationMsg_13": false,
                    "outsideCancelPolicyMsgKey": null,
                    "insideCancelPolicyMsgKey": "cancellation.inside.NightFullPenalty.b",
                    "agencyReserveNowPayLater": false,
                    "showCancelPolicy": true,
                    "insideFeePenaltyText": "US$0.00",
                    "outsideFeePenaltyText": "US$0.00",
                    "showNightlyRates": false,
                    "drrExpirationSecsText": "1884419416",
                    "drrExpiration_1": false,
                    "drrExpiration_2": false,
                    "drrExpiration_3": false,
                    "drrExpiration_4": true,
                    "airAttach": false,
                    "outsideWindowPrice": false,
                    "insideWindowPrice": false,
                    "showETPDepositChoice": false,
                    "drrDiscountPercentageBased": false,
                    "hasValueAdd": false,
                    "validDRRForExp15881": false,
                    "dealOfTheDayDRRPresent": false,
                    "thirdPartyInventoryProvider": false,
                    "displayMultiSourceToolTip": false,
                    "refundable": true,
                    "isDisplayHPG": true,
                    "loyaltyPointsEnabled": false,
                    "freeOnlineCancellation": false,
                    "mrp": false
                },
                    {
                    "nightlyRates": [],
                    "hotelID": "33204043",
                    "roomTypeCode": "213605640",
                    "ratePlanCode": "244100589",
                    "piid": "LPASTESTPIID_V3",
                    "roomName": "",
                    "activityID": "1c4bacb5-b193-4719-979c-adf5ef5414a3",
                    "numberOfNights": 1,
                    "insideWindowPenaltyNightCount": 1,
                    "insideWindowPenaltyPercentage": 0,
                    "outsideWindowPenaltyNightCount": 0,
                    "outsideWindowPenaltyPercentage": 0,
                    "cancellationWindowDate": "9月19日星期四",
                    "cancellationWindowTime": "18:00",
                    "cancellationTimeZoneName": "中国标准时间",
                    "feePenalty": {
                        "amount": 0.00,
                        "currency": "USD",
                        "currencyCode": "USD",
                        "negative": false,
                        "double": 0.0
                    },
                    "insideFeePenalty": {
                        "amount": 0.00,
                        "currency": "USD",
                        "currencyCode": "USD",
                        "negative": false,
                        "double": 0.0
                    },
                    "checkInDate": "2019/09/20",
                    "checkOutDate": "2019/09/21",
                    "offerType": "5",
                    "maxGuests": 0,
                    "maxAdults": 0,
                    "maxChildren": 0,
                    "showETPTooltip": true,
                    "minGuestAge": 0,
                    "numberOfRoomsLeft": 0,
                    "price": {
                        "available": true,
                        "displayPrice": "CNY521",
                        "chargedDisplayPrice": "US$73",
                        "crossOutPrice": null,
                        "totalPriceWithoutMandatoryFee": 0.0,
                        "perPersonTotalPrice": 0.0,
                        "perNightTotalPrice": 0.0,
                        "formattedDiscountAmount": null,
                        "formattedTotalLoyaltyPoints": null,
                        "percentageDiscount": 0,
                        "discountAmount": 0,
                        "totalPrice": 520.58,
                        "displayViewTotalPrice": false,
                        "oneNightStay": false,
                        "expediaPointsBranded": "Expedia+ 积分",
                        "displayTotalPriceWithTaxesAndFees": "CNY607",
                        "chargedDisplayTotalPriceWithTaxesAndFees": "US$86",
                        "isPackageSavingsSignificant": false,
                        "displayTotalPrice": "CNY521",
                        "priceObject": {
                            "amount": 520.58,
                            "currency": "CNY",
                            "currencyCode": "CNY",
                            "negative": false,
                            "double": 520.58
                        },
                        "packageSavingsSignificant": false,
                        "price": 520.58,
                        "unformattedCrossOutPrice": 0.0,
                        "unformattedTotalPrice": "520.58"
                    },
                    "totalPriceWithTaxesAndFees": {
                        "amount": 606.99,
                        "currency": "CNY",
                        "currencyCode": "CNY",
                        "negative": false,
                        "double": 606.99
                    },
                    "currencyPosa": "CNY",
                    "currencyPosu": "CNY",
                    "billingCurrencyCode": "USD",
                    "quotedRate": 520.58,
                    "resortFee": null,
                    "taxableServiceFee": null,
                    "taxesAndFeesNotIncludedInPrice": {
                        "amount": 86.41,
                        "currency": "CNY",
                        "currencyCode": "CNY",
                        "negative": false,
                        "double": 86.41
                    },
                    "totalWithCityTax": {
                        "amount": 693.40,
                        "currency": "CNY",
                        "currencyCode": "CNY",
                        "negative": false,
                        "double": 693.4
                    },
                    "drrId": 0,
                    "showMemberDiscountBadge": true,
                    "drrMessage": "",
                    "drrExpirationSecs": 1884419416,
                    "drrExpirationDate": "2079/6/6",
                    "tonightOnlyDRRSaveValue": "",
                    "valueAdd": {},
                    "loyaltyEarnPoints": null,
                    "earnRewardsForGPS": null,
                    "earnRewardsText": null,
                    "drrMessageForGPSEnabled": false,
                    "earnRewardsGPSLogoEnabled": false,
                    "exclusiveOfferMsg": null,
                    "loyaltyEarnPrice": null,
                    "loyaltyBurnedPrice": null,
                    "totalLoyaltyBurnedPriceWithTaxesAndFees": null,
                    "loyaltyCrossOutPrice": null,
                    "totalLoyaltyCrossOutPriceWithTaxesAndFees": null,
                    "includedFees": {
                        "fees": [],
                        "displayTotal": null,
                        "totalAmount": 0,
                        "showMandatoryFee": false,
                        "usePOSuCurrency": false
                    },
                    "excludedFees": {
                        "fees": [],
                        "displayTotal": null,
                        "totalAmount": 0,
                        "showMandatoryFee": false,
                        "usePOSuCurrency": false
                    },
                    "homeAwayRDD": null,
                    "homeAwayRDDIncluded": false,
                    "amenities": {},
                    "inventoryProviderID": 24,
                    "loyaltyBaseEarnPrice": null,
                    "loyaltyBonusEarnPrice": null,
                    "earnModifierOperation": null,
                    "earnModifierValue": null,
                    "eligibleForTaapDeferredPayment": false,
                    "taapDeferredPaymentDateWindow": null,
                    "airAttachDiscountPercentage": null,
                    "conversionNeeded": true,
                    "displayNightlyRateDisclaimer": false,
                    "travelerServiceFee": null,
                    "travelerAndTaxableServiceFee": null,
                    "cartId": null,
                    "bundleId": null,
                    "containsL26Taxes": false,
                    "shpmDiscountModel": null,
                    "roomOccupants": "rm1=a2",
                    "multiItem": false,
                    "multiCurrencyEnabled": true,
                    "payLater": true,
                    "nonRefundableInsideWindow": true,
                    "nonRefundableOutsideWindow": false,
                    "paymentChoiceAvailable": true,
                    "priceModified": false,
                    "artificiallyFencedRate": false,
                    "bookable": true,
                    "udp": true,
                    "multiCurrencyBillingEnabled": true,
                    "drrpresent": false,
                    "tonightOnlyDRRPresent": false,
                    "promoMsgEnabledHIS": false,
                    "memberExclusiveDRRPresent": false,
                    "memberExclusiveDRRAvailable": false,
                    "mobileExclusive": false,
                    "removeDrrTooltip": false,
                    "showTdEarnMessage": false,
                    "modHisMeatStickerEnabled": false,
                    "showCancellationMsg_1": false,
                    "showCancellationMsg_1_v2": false,
                    "showCancellationMsg_2": false,
                    "showCancellationMsg_2_v2": false,
                    "showCancellationMsg_3": false,
                    "showCancellationMsg_3_v2": false,
                    "showCancellationMsg_4": false,
                    "showCancellationMsg_4_v2": false,
                    "showCancellationMsg_5": false,
                    "showCancellationMsg_5_v2": false,
                    "showCancellationMsg_6": false,
                    "showCancellationMsg_6_v2": false,
                    "showCancellationMsg_7": false,
                    "showCancellationMsg_7_v2": true,
                    "showCancellationMsg_8": false,
                    "showCancellationMsg_8_v2": false,
                    "showCancellationMsg_9": false,
                    "showCancellationMsg_9_v2": false,
                    "showCancellationMsg_10": false,
                    "showCancellationMsg_10_v2": false,
                    "showCancellationMsg_11": false,
                    "showCancellationMsg_11_v2": false,
                    "showCancellationMsg_12": false,
                    "showCancellationMsg_13": false,
                    "outsideCancelPolicyMsgKey": null,
                    "insideCancelPolicyMsgKey": "cancellation.inside.NightFullPenalty.b",
                    "agencyReserveNowPayLater": false,
                    "showCancelPolicy": true,
                    "insideFeePenaltyText": "US$0.00",
                    "outsideFeePenaltyText": "US$0.00",
                    "showNightlyRates": false,
                    "drrExpirationSecsText": "1884419416",
                    "drrExpiration_1": false,
                    "drrExpiration_2": false,
                    "drrExpiration_3": false,
                    "drrExpiration_4": true,
                    "airAttach": false,
                    "outsideWindowPrice": false,
                    "insideWindowPrice": false,
                    "showETPDepositChoice": false,
                    "drrDiscountPercentageBased": false,
                    "hasValueAdd": false,
                    "validDRRForExp15881": false,
                    "dealOfTheDayDRRPresent": false,
                    "thirdPartyInventoryProvider": false,
                    "displayMultiSourceToolTip": false,
                    "refundable": true,
                    "isDisplayHPG": true,
                    "loyaltyPointsEnabled": false,
                    "freeOnlineCancellation": false,
                    "mrp": false
                },
                    {
                    "nightlyRates": [],
                    "hotelID": "33204043",
                    "roomTypeCode": "213605640",
                    "ratePlanCode": "244100589",
                    "piid": "LPASTESTPIID_V3",
                    "roomName": "",
                    "activityID": "1c4bacb5-b193-4719-979c-adf5ef5414a3",
                    "numberOfNights": 1,
                    "insideWindowPenaltyNightCount": 1,
                    "insideWindowPenaltyPercentage": 0,
                    "outsideWindowPenaltyNightCount": 0,
                    "outsideWindowPenaltyPercentage": 0,
                    "cancellationWindowDate": "9月19日星期四",
                    "cancellationWindowTime": "18:00",
                    "cancellationTimeZoneName": "中国标准时间",
                    "feePenalty": {
                        "amount": 0.00,
                        "currency": "USD",
                        "currencyCode": "USD",
                        "negative": false,
                        "double": 0.0
                    },
                    "insideFeePenalty": {
                        "amount": 0.00,
                        "currency": "USD",
                        "currencyCode": "USD",
                        "negative": false,
                        "double": 0.0
                    },
                    "checkInDate": "2019/09/20",
                    "checkOutDate": "2019/09/21",
                    "offerType": "1",
                    "maxGuests": 0,
                    "maxAdults": 0,
                    "maxChildren": 0,
                    "showETPTooltip": true,
                    "minGuestAge": 0,
                    "numberOfRoomsLeft": 0,
                    "price": {
                        "available": true,
                        "displayPrice": "CNY521",
                        "chargedDisplayPrice": "US$73",
                        "crossOutPrice": null,
                        "totalPriceWithoutMandatoryFee": 0.0,
                        "perPersonTotalPrice": 0.0,
                        "perNightTotalPrice": 0.0,
                        "formattedDiscountAmount": null,
                        "formattedTotalLoyaltyPoints": null,
                        "percentageDiscount": 0,
                        "discountAmount": 0,
                        "totalPrice": 520.61,
                        "displayViewTotalPrice": false,
                        "oneNightStay": false,
                        "expediaPointsBranded": "Expedia+ 积分",
                        "displayTotalPriceWithTaxesAndFees": "CNY607",
                        "chargedDisplayTotalPriceWithTaxesAndFees": "US$86",
                        "isPackageSavingsSignificant": false,
                        "displayTotalPrice": "CNY521",
                        "priceObject": {
                            "amount": 520.61,
                            "currency": "CNY",
                            "currencyCode": "CNY",
                            "negative": false,
                            "double": 520.61
                        },
                        "packageSavingsSignificant": false,
                        "price": 520.61,
                        "unformattedCrossOutPrice": 0.0,
                        "unformattedTotalPrice": "520.61"
                    },
                    "totalPriceWithTaxesAndFees": {
                        "amount": 606.99,
                        "currency": "CNY",
                        "currencyCode": "CNY",
                        "negative": false,
                        "double": 606.99
                    },
                    "currencyPosa": "CNY",
                    "currencyPosu": "CNY",
                    "billingCurrencyCode": "USD",
                    "quotedRate": 520.61,
                    "resortFee": null,
                    "taxableServiceFee": null,
                    "taxesAndFeesNotIncludedInPrice": {
                        "amount": 86.38,
                        "currency": "CNY",
                        "currencyCode": "CNY",
                        "negative": false,
                        "double": 86.38
                    },
                    "totalWithCityTax": {
                        "amount": 693.37,
                        "currency": "CNY",
                        "currencyCode": "CNY",
                        "negative": false,
                        "double": 693.37
                    },
                    "drrId": 0,
                    "showMemberDiscountBadge": true,
                    "drrMessage": "",
                    "drrExpirationSecs": 1884419416,
                    "drrExpirationDate": "2079/6/6",
                    "tonightOnlyDRRSaveValue": "",
                    "valueAdd": {},
                    "loyaltyEarnPoints": null,
                    "earnRewardsForGPS": null,
                    "earnRewardsText": null,
                    "drrMessageForGPSEnabled": false,
                    "earnRewardsGPSLogoEnabled": false,
                    "exclusiveOfferMsg": null,
                    "loyaltyEarnPrice": null,
                    "loyaltyBurnedPrice": null,
                    "totalLoyaltyBurnedPriceWithTaxesAndFees": null,
                    "loyaltyCrossOutPrice": null,
                    "totalLoyaltyCrossOutPriceWithTaxesAndFees": null,
                    "includedFees": {
                        "fees": [],
                        "displayTotal": null,
                        "totalAmount": 0,
                        "showMandatoryFee": false,
                        "usePOSuCurrency": false
                    },
                    "excludedFees": {
                        "fees": [],
                        "displayTotal": null,
                        "totalAmount": 0,
                        "showMandatoryFee": false,
                        "usePOSuCurrency": false
                    },
                    "homeAwayRDD": null,
                    "homeAwayRDDIncluded": false,
                    "amenities": {},
                    "inventoryProviderID": 24,
                    "loyaltyBaseEarnPrice": null,
                    "loyaltyBonusEarnPrice": null,
                    "earnModifierOperation": null,
                    "earnModifierValue": null,
                    "eligibleForTaapDeferredPayment": false,
                    "taapDeferredPaymentDateWindow": null,
                    "airAttachDiscountPercentage": null,
                    "conversionNeeded": true,
                    "displayNightlyRateDisclaimer": false,
                    "travelerServiceFee": null,
                    "travelerAndTaxableServiceFee": null,
                    "cartId": null,
                    "bundleId": null,
                    "containsL26Taxes": false,
                    "shpmDiscountModel": null,
                    "roomOccupants": "rm1=a2",
                    "multiItem": false,
                    "multiCurrencyEnabled": true,
                    "payLater": false,
                    "nonRefundableInsideWindow": true,
                    "nonRefundableOutsideWindow": false,
                    "paymentChoiceAvailable": true,
                    "priceModified": false,
                    "artificiallyFencedRate": false,
                    "bookable": true,
                    "udp": true,
                    "multiCurrencyBillingEnabled": true,
                    "drrpresent": false,
                    "tonightOnlyDRRPresent": false,
                    "promoMsgEnabledHIS": false,
                    "memberExclusiveDRRPresent": false,
                    "memberExclusiveDRRAvailable": false,
                    "mobileExclusive": false,
                    "removeDrrTooltip": false,
                    "showTdEarnMessage": false,
                    "modHisMeatStickerEnabled": false,
                    "showCancellationMsg_1": false,
                    "showCancellationMsg_1_v2": false,
                    "showCancellationMsg_2": false,
                    "showCancellationMsg_2_v2": false,
                    "showCancellationMsg_3": false,
                    "showCancellationMsg_3_v2": false,
                    "showCancellationMsg_4": false,
                    "showCancellationMsg_4_v2": false,
                    "showCancellationMsg_5": false,
                    "showCancellationMsg_5_v2": false,
                    "showCancellationMsg_6": false,
                    "showCancellationMsg_6_v2": false,
                    "showCancellationMsg_7": false,
                    "showCancellationMsg_7_v2": true,
                    "showCancellationMsg_8": false,
                    "showCancellationMsg_8_v2": false,
                    "showCancellationMsg_9": false,
                    "showCancellationMsg_9_v2": false,
                    "showCancellationMsg_10": false,
                    "showCancellationMsg_10_v2": false,
                    "showCancellationMsg_11": false,
                    "showCancellationMsg_11_v2": false,
                    "showCancellationMsg_12": false,
                    "showCancellationMsg_13": false,
                    "outsideCancelPolicyMsgKey": null,
                    "insideCancelPolicyMsgKey": "cancellation.inside.NightFullPenalty.b",
                    "agencyReserveNowPayLater": false,
                    "showCancelPolicy": true,
                    "insideFeePenaltyText": "US$0.00",
                    "outsideFeePenaltyText": "US$0.00",
                    "showNightlyRates": false,
                    "drrExpirationSecsText": "1884419416",
                    "drrExpiration_1": false,
                    "drrExpiration_2": false,
                    "drrExpiration_3": false,
                    "drrExpiration_4": true,
                    "airAttach": false,
                    "outsideWindowPrice": false,
                    "insideWindowPrice": false,
                    "showETPDepositChoice": false,
                    "drrDiscountPercentageBased": false,
                    "hasValueAdd": false,
                    "validDRRForExp15881": false,
                    "dealOfTheDayDRRPresent": false,
                    "thirdPartyInventoryProvider": false,
                    "displayMultiSourceToolTip": false,
                    "refundable": true,
                    "isDisplayHPG": true,
                    "loyaltyPointsEnabled": false,
                    "freeOnlineCancellation": false,
                    "mrp": false
                },
                    {
                    "nightlyRates": [],
                    "hotelID": "33204043",
                    "roomTypeCode": "213605641",
                    "ratePlanCode": "244100590",
                    "piid": "LPASTESTPIID_V3",
                    "roomName": "",
                    "activityID": "1c4bacb5-b193-4719-979c-adf5ef5414a3",
                    "numberOfNights": 1,
                    "insideWindowPenaltyNightCount": 1,
                    "insideWindowPenaltyPercentage": 0,
                    "outsideWindowPenaltyNightCount": 0,
                    "outsideWindowPenaltyPercentage": 0,
                    "cancellationWindowDate": "9月19日星期四",
                    "cancellationWindowTime": "18:00",
                    "cancellationTimeZoneName": "中国标准时间",
                    "feePenalty": {
                        "amount": 0.00,
                        "currency": "USD",
                        "currencyCode": "USD",
                        "negative": false,
                        "double": 0.0
                    },
                    "insideFeePenalty": {
                        "amount": 0.00,
                        "currency": "USD",
                        "currencyCode": "USD",
                        "negative": false,
                        "double": 0.0
                    },
                    "checkInDate": "2019/09/20",
                    "checkOutDate": "2019/09/21",
                    "offerType": "5",
                    "maxGuests": 0,
                    "maxAdults": 0,
                    "maxChildren": 0,
                    "showETPTooltip": false,
                    "minGuestAge": 9223372036854775807,
                    "numberOfRoomsLeft": 0,
                    "price": null,
                    "totalPriceWithTaxesAndFees": null,
                    "currencyPosa": null,
                    "currencyPosu": null,
                    "billingCurrencyCode": null,
                    "quotedRate": null,
                    "resortFee": null,
                    "taxableServiceFee": null,
                    "taxesAndFeesNotIncludedInPrice": null,
                    "totalWithCityTax": null,
                    "drrId": null,
                    "showMemberDiscountBadge": false,
                    "drrMessage": "",
                    "drrExpirationSecs": 0,
                    "drrExpirationDate": null,
                    "tonightOnlyDRRSaveValue": null,
                    "valueAdd": {},
                    "loyaltyEarnPoints": null,
                    "earnRewardsForGPS": null,
                    "earnRewardsText": null,
                    "drrMessageForGPSEnabled": false,
                    "earnRewardsGPSLogoEnabled": false,
                    "exclusiveOfferMsg": null,
                    "loyaltyEarnPrice": null,
                    "loyaltyBurnedPrice": null,
                    "totalLoyaltyBurnedPriceWithTaxesAndFees": null,
                    "loyaltyCrossOutPrice": null,
                    "totalLoyaltyCrossOutPriceWithTaxesAndFees": null,
                    "includedFees": {
                        "fees": [],
                        "displayTotal": null,
                        "totalAmount": 0,
                        "showMandatoryFee": false,
                        "usePOSuCurrency": false
                    },
                    "excludedFees": {
                        "fees": [],
                        "displayTotal": null,
                        "totalAmount": 0,
                        "showMandatoryFee": false,
                        "usePOSuCurrency": false
                    },
                    "homeAwayRDD": null,
                    "homeAwayRDDIncluded": false,
                    "amenities": {},
                    "inventoryProviderID": 24,
                    "loyaltyBaseEarnPrice": null,
                    "loyaltyBonusEarnPrice": null,
                    "earnModifierOperation": null,
                    "earnModifierValue": null,
                    "eligibleForTaapDeferredPayment": false,
                    "taapDeferredPaymentDateWindow": null,
                    "airAttachDiscountPercentage": null,
                    "conversionNeeded": false,
                    "displayNightlyRateDisclaimer": false,
                    "travelerServiceFee": null,
                    "travelerAndTaxableServiceFee": null,
                    "cartId": null,
                    "bundleId": null,
                    "containsL26Taxes": false,
                    "shpmDiscountModel": null,
                    "roomOccupants": "rm1=a2",
                    "multiItem": false,
                    "multiCurrencyEnabled": false,
                    "payLater": false,
                    "nonRefundableInsideWindow": true,
                    "nonRefundableOutsideWindow": false,
                    "paymentChoiceAvailable": false,
                    "priceModified": false,
                    "artificiallyFencedRate": false,
                    "udp": true,
                    "multiCurrencyBillingEnabled": false,
                    "drrpresent": false,
                    "tonightOnlyDRRPresent": false,
                    "promoMsgEnabledHIS": false,
                    "memberExclusiveDRRPresent": false,
                    "memberExclusiveDRRAvailable": false,
                    "mobileExclusive": false,
                    "soldOut": true,
                    "removeDrrTooltip": false,
                    "showTdEarnMessage": false,
                    "modHisMeatStickerEnabled": false,
                    "showCancellationMsg_1": false,
                    "showCancellationMsg_1_v2": false,
                    "showCancellationMsg_2": false,
                    "showCancellationMsg_2_v2": false,
                    "showCancellationMsg_3": false,
                    "showCancellationMsg_3_v2": false,
                    "showCancellationMsg_4": false,
                    "showCancellationMsg_4_v2": false,
                    "showCancellationMsg_5": false,
                    "showCancellationMsg_5_v2": false,
                    "showCancellationMsg_6": false,
                    "showCancellationMsg_6_v2": false,
                    "showCancellationMsg_7": false,
                    "showCancellationMsg_7_v2": true,
                    "showCancellationMsg_8": false,
                    "showCancellationMsg_8_v2": false,
                    "showCancellationMsg_9": false,
                    "showCancellationMsg_9_v2": false,
                    "showCancellationMsg_10": false,
                    "showCancellationMsg_10_v2": false,
                    "showCancellationMsg_11": false,
                    "showCancellationMsg_11_v2": false,
                    "showCancellationMsg_12": false,
                    "showCancellationMsg_13": false,
                    "outsideCancelPolicyMsgKey": null,
                    "insideCancelPolicyMsgKey": "cancellation.inside.NightFullPenalty.b",
                    "agencyReserveNowPayLater": false,
                    "showCancelPolicy": true,
                    "insideFeePenaltyText": "US$0.00",
                    "outsideFeePenaltyText": "US$0.00",
                    "showNightlyRates": false,
                    "drrExpirationSecsText": "0",
                    "drrExpiration_1": false,
                    "drrExpiration_2": false,
                    "drrExpiration_3": false,
                    "drrExpiration_4": false,
                    "airAttach": false,
                    "outsideWindowPrice": false,
                    "insideWindowPrice": false,
                    "showETPDepositChoice": false,
                    "drrDiscountPercentageBased": false,
                    "hasValueAdd": false,
                    "validDRRForExp15881": false,
                    "dealOfTheDayDRRPresent": false,
                    "thirdPartyInventoryProvider": false,
                    "displayMultiSourceToolTip": false,
                    "refundable": true,
                    "isDisplayHPG": true,
                    "loyaltyPointsEnabled": false,
                    "freeOnlineCancellation": false,
                    "mrp": false
                },
                    {
                    "nightlyRates": [],
                    "hotelID": "33204043",
                    "roomTypeCode": "213605642",
                    "ratePlanCode": "244100591",
                    "piid": "LPASTESTPIID_V3",
                    "roomName": "",
                    "activityID": "1c4bacb5-b193-4719-979c-adf5ef5414a3",
                    "numberOfNights": 1,
                    "insideWindowPenaltyNightCount": 1,
                    "insideWindowPenaltyPercentage": 0,
                    "outsideWindowPenaltyNightCount": 0,
                    "outsideWindowPenaltyPercentage": 0,
                    "cancellationWindowDate": "9月19日星期四",
                    "cancellationWindowTime": "18:00",
                    "cancellationTimeZoneName": "中国标准时间",
                    "feePenalty": {
                        "amount": 0.00,
                        "currency": "USD",
                        "currencyCode": "USD",
                        "negative": false,
                        "double": 0.0
                    },
                    "insideFeePenalty": {
                        "amount": 0.00,
                        "currency": "USD",
                        "currencyCode": "USD",
                        "negative": false,
                        "double": 0.0
                    },
                    "checkInDate": "2019/09/20",
                    "checkOutDate": "2019/09/21",
                    "offerType": "5",
                    "maxGuests": 0,
                    "maxAdults": 0,
                    "maxChildren": 0,
                    "showETPTooltip": false,
                    "minGuestAge": 9223372036854775807,
                    "numberOfRoomsLeft": 0,
                    "price": null,
                    "totalPriceWithTaxesAndFees": null,
                    "currencyPosa": null,
                    "currencyPosu": null,
                    "billingCurrencyCode": null,
                    "quotedRate": null,
                    "resortFee": null,
                    "taxableServiceFee": null,
                    "taxesAndFeesNotIncludedInPrice": null,
                    "totalWithCityTax": null,
                    "drrId": null,
                    "showMemberDiscountBadge": false,
                    "drrMessage": "",
                    "drrExpirationSecs": 0,
                    "drrExpirationDate": null,
                    "tonightOnlyDRRSaveValue": null,
                    "valueAdd": {},
                    "loyaltyEarnPoints": null,
                    "earnRewardsForGPS": null,
                    "earnRewardsText": null,
                    "drrMessageForGPSEnabled": false,
                    "earnRewardsGPSLogoEnabled": false,
                    "exclusiveOfferMsg": null,
                    "loyaltyEarnPrice": null,
                    "loyaltyBurnedPrice": null,
                    "totalLoyaltyBurnedPriceWithTaxesAndFees": null,
                    "loyaltyCrossOutPrice": null,
                    "totalLoyaltyCrossOutPriceWithTaxesAndFees": null,
                    "includedFees": {
                        "fees": [],
                        "displayTotal": null,
                        "totalAmount": 0,
                        "showMandatoryFee": false,
                        "usePOSuCurrency": false
                    },
                    "excludedFees": {
                        "fees": [],
                        "displayTotal": null,
                        "totalAmount": 0,
                        "showMandatoryFee": false,
                        "usePOSuCurrency": false
                    },
                    "homeAwayRDD": null,
                    "homeAwayRDDIncluded": false,
                    "amenities": {},
                    "inventoryProviderID": 24,
                    "loyaltyBaseEarnPrice": null,
                    "loyaltyBonusEarnPrice": null,
                    "earnModifierOperation": null,
                    "earnModifierValue": null,
                    "eligibleForTaapDeferredPayment": false,
                    "taapDeferredPaymentDateWindow": null,
                    "airAttachDiscountPercentage": null,
                    "conversionNeeded": false,
                    "displayNightlyRateDisclaimer": false,
                    "travelerServiceFee": null,
                    "travelerAndTaxableServiceFee": null,
                    "cartId": null,
                    "bundleId": null,
                    "containsL26Taxes": false,
                    "shpmDiscountModel": null,
                    "roomOccupants": "rm1=a2",
                    "multiItem": false,
                    "multiCurrencyEnabled": false,
                    "payLater": false,
                    "nonRefundableInsideWindow": true,
                    "nonRefundableOutsideWindow": false,
                    "paymentChoiceAvailable": false,
                    "priceModified": false,
                    "artificiallyFencedRate": false,
                    "udp": true,
                    "multiCurrencyBillingEnabled": false,
                    "drrpresent": false,
                    "tonightOnlyDRRPresent": false,
                    "promoMsgEnabledHIS": false,
                    "memberExclusiveDRRPresent": false,
                    "memberExclusiveDRRAvailable": false,
                    "mobileExclusive": false,
                    "soldOut": true,
                    "removeDrrTooltip": false,
                    "showTdEarnMessage": false,
                    "modHisMeatStickerEnabled": false,
                    "showCancellationMsg_1": false,
                    "showCancellationMsg_1_v2": false,
                    "showCancellationMsg_2": false,
                    "showCancellationMsg_2_v2": false,
                    "showCancellationMsg_3": false,
                    "showCancellationMsg_3_v2": false,
                    "showCancellationMsg_4": false,
                    "showCancellationMsg_4_v2": false,
                    "showCancellationMsg_5": false,
                    "showCancellationMsg_5_v2": false,
                    "showCancellationMsg_6": false,
                    "showCancellationMsg_6_v2": false,
                    "showCancellationMsg_7": false,
                    "showCancellationMsg_7_v2": true,
                    "showCancellationMsg_8": false,
                    "showCancellationMsg_8_v2": false,
                    "showCancellationMsg_9": false,
                    "showCancellationMsg_9_v2": false,
                    "showCancellationMsg_10": false,
                    "showCancellationMsg_10_v2": false,
                    "showCancellationMsg_11": false,
                    "showCancellationMsg_11_v2": false,
                    "showCancellationMsg_12": false,
                    "showCancellationMsg_13": false,
                    "outsideCancelPolicyMsgKey": null,
                    "insideCancelPolicyMsgKey": "cancellation.inside.NightFullPenalty.b",
                    "agencyReserveNowPayLater": false,
                    "showCancelPolicy": true,
                    "insideFeePenaltyText": "US$0.00",
                    "outsideFeePenaltyText": "US$0.00",
                    "showNightlyRates": false,
                    "drrExpirationSecsText": "0",
                    "drrExpiration_1": false,
                    "drrExpiration_2": false,
                    "drrExpiration_3": false,
                    "drrExpiration_4": false,
                    "airAttach": false,
                    "outsideWindowPrice": false,
                    "insideWindowPrice": false,
                    "showETPDepositChoice": false,
                    "drrDiscountPercentageBased": false,
                    "hasValueAdd": false,
                    "validDRRForExp15881": false,
                    "dealOfTheDayDRRPresent": false,
                    "thirdPartyInventoryProvider": false,
                    "displayMultiSourceToolTip": false,
                    "refundable": true,
                    "isDisplayHPG": true,
                    "loyaltyPointsEnabled": false,
                    "freeOnlineCancellation": false,
                    "mrp": false
                }],
                "fromStayDate": "2019-09-20",
                "toStayDate": "2019-09-21",
                "formattedFromStayDate": "9月20日星期五",
                "formattedToStayDate": "9月21日星期六",
                "formattedShortFromStayDate": "9月20日",
                "formattedShortToStayDate": "9月21日",
                "soldOutRoomTypes": ["213605641", "213605642"],
                "travelerData": {
                    "chkin": "2019/09/20",
                    "chkout": "2019/09/21",
                    "adults": "2",
                    "children": "0",
                    "childAge": null,
                    "brandId": "4899",
                    "packageType": null,
                    "countryId": 37,
                    "isVip": false,
                    "swpToggleOn": null,
                    "cacheId": null,
                    "tla": "HGH",
                    "stayLength": null,
                    "daysInFuture": null,
                    "ticketedTravelers": null,
                    "evalMODExp": true,
                    "partnerName": "",
                    "partnerPrice": "0.0",
                    "partnerCurrency": "",
                    "partnerTimestamp": "0",
                    "cartId": null,
                    "cancellable": "false"
                },
                "taapPackageRateEnabled": false,
                "loyaltyData": {
                    "rewardsAmount": 0,
                    "formattedRewardsAmount": null,
                    "rewardsDollarValue": null,
                    "redemptionFloorAmount": 0,
                    "expediaPlusBranded": "Expedia Rewards",
                    "expediaPointsBranded": "Expedia+ 积分",
                    "awardType": "points",
                    "hasLoyaltyEarnings": null,
                    "hasGPSLoyaltyEarnings": false,
                    "tier": null,
                    "swpToggleDefaultState": false,
                    "canUserBurn": false,
                    "displaySwpToggle": null
                },
                "displayQualifyingNights": true,
                "showExcludeTaxMessage": false,
                "showNoRefundIcon": false,
                "drrMessageForGPSEnabled": false,
                "omnitureData": {
                    "pageName": "page.Hotels.Infosite.Information",
                    "channel": "hotels",
                    "products": ";Hotel:33204043;;",
                    "events": "event3,event10,event18",
                    "prop2": "hotels",
                    "eVar2": "D=c2",
                    "prop5": "2019-09-20",
                    "prop6": "2019-09-21",
                    "eVar5": "1",
                    "eVar6": "1",
                    "list1": "26334.0|26095.0|30867.1|11233.1|15196.1|26376.0|31164.0|31198.0|11423.1|16373.1|24578.1|30546.1|13070.0|24833.1|12227.0|14251.0|16215.1|26391.1|30251.0|16155.1|26138.1|31186.0|30442.1|14990.1|30868.1|99991.0|16016.0|29193.1",
                    "prop46": "24:4",
                    "prop19": "3PI:NA|ESR:439|PDT:NA|PDTP:NA|PD:NA|PDP:NA",
                    "eVar55": "anonymous | ",
                    "eVar40": "NoPartnerTier",
                    "omnitureFeeInformation": {
                        "244100589": "event296",
                        "244100588": "event296",
                        "244100591": "event296",
                        "244100590": "event296"
                    }
                },
                "displayTotalPrice": false,
                "showEarnPointsWithDecimals": false,
                "shoppedTspids": [24],
                "groModRebrandEnabled": false,
                "groModWhiteRebrandEnabled": false,
                "groModWhiteRebrandForGuestEnabled": false,
                "showPersFailureErrorMessage": false,
                "drrpresent": false,
                "mobileOnlyDRRPresent": false,
                "tonightOnlyDRRPresent": false,
                "hotelSoldOut": false,
                "showViewTotalPrice": false
            };
            infosite.parsedOffersData = {};
            infosite.commitHash = "4dea5eb17176c958ce3aeeeef50ad7fb05c3c0c4";
            infosite.awsRegionName = "us-east-1";
            infosite.reviewSummaryData = {
                assuranceText: '',
                isVerifiedReviews: true,
                reviewIconUrl: 'https://a.travel-assets.com/dms-svg/ugc/verified_reviews_icon.svg',
                brandName: 'Expedia 亿客行',
                rfrrBase: 'HOT.HIS.',
                totalRating: 5,
                hotelName: '杭州西湖武林广场亚朵轻居酒店 '
            };
            infosite.reviewListData = {
                displayBrandWithDatePosted: 'true' === 'true',
                isTravelocity: 'false' === 'true',
                baseURL: '/ugc/urs/api',
            };
            infosite.defaultServiceTimeout = 10000;
            infosite.scratchpadUrgencyRegionWhitelist = [];
            infosite.scratchpadUrgencyRegionWhitelist.push(178276);
            infosite.scratchpadUrgencyRegionWhitelist.push(178293);
            infosite.scratchpadUrgencyRegionWhitelist.push(178294);
            infosite.scratchpadUrgencyRegionWhitelist.push(178286);
            infosite.scratchpadUrgencyRegionWhitelist.push(178280);
            infosite.scratchpadUrgencyRegionWhitelist.push(178304);
            infosite.scratchpadUrgencyRegionWhitelist.push(178248);
            infosite.scratchpadUrgencyRegionWhitelist.push(178305);
            infosite.scratchpadUrgencyRegionWhitelist.push(180077);
            infosite.scratchpadUrgencyRegionWhitelist.push(601685);
            infosite.scratchpadUrgencyRegionWhitelist.push(178239);
            infosite.scratchpadUrgencyRegionWhitelist.push(178318);
            infosite.scratchpadUrgencyRegionWhitelist.push(178307);
            infosite.scratchpadUrgencyRegionWhitelist.push(603224);
            infosite.scratchpadUrgencyRegionWhitelist.push(178292);
            infosite.scratchpadUrgencyRegionWhitelist.push(601750);
            infosite.scratchpadUrgencyRegionWhitelist.push(178232);
            infosite.scratchpadUrgencyRegionWhitelist.push(800045);
            infosite.scratchpadUrgencyRegionWhitelist.push(180073);
            infosite.scratchpadUrgencyRegionWhitelist.push(6023765);
            infosite.partnerName = '';
            infosite.partnerPrice = '0';
            infosite.partnerCurrency = '';
            infosite.partnerTimestamp = '0';
            infosite.showHotwireDealsBanner = false;
            infosite.listSaveEnabled = true;
            infosite.isOmnitureSessionInfoCallEnabled = false;
            infosite.showPointsTextAsPtsEnabled = false;
// START Experiment 26344 LShop_AFR_MktRebal_SupplierFund
            infosite.isMarketRebalanceHotel = false;
// END Experiment 26344 LShop_AFR_MktRebal_SupplierFund
// begin exp24510
            infosite.UGCUrl = "https://apim.expedia.com/reviews1y/ugc/search";
            infosite.UGCKey = "b58bdcd1-a6c9-47e9-b171-ed9fefa8131e";
// end exp24510
// Begin 27237 HIS_Graceland_ShowCancelInRoomRateViewV2
// End 27237 HIS_Graceland_ShowCancelInRoomRateViewV2
//Begin Exp 26305 TAAP_Package_Rates_Directly_from_LPS
            infosite.taapPackageRates = false;
//End 26305 TAAP_Package_Rates_Directly_from_LPS
            infosite.showTotalpriceQualifierMessage = false;
            infosite.showMandatoryFeesTooltip = true;
            return infosite;
        });
        require(['infosite', 'uitk'], function (infosite, uitk) {
            uitk.subscribe('mediaquery.matched', infosite, function (topic, data) {
                if (data.key === 'mobile') {
                    this.isMobilePhone = true;
                    $('body').addClass('mobileCollapseWizard');
                }
            });
            uitk.mediaquery.publishAgain();
        });
        define('homeAwayPropertyDescription', [], function () {
            return {
                run: function () {
                }
            };
        });
        define("subscribeView", ["marionette", "uitk", "infositeData", "jquery"], function (e, t, i, s) {
            "use strict";

            function n() {
                require("scratchpad", function (e) {
                    e.enrollInNudge()
                });
                var e = s(".post-state-msg");
                s("#subscribe-button").addClass("hidden"), t.utils.focusElement(e.removeClass("hidden")), t.utils.liveAnnounce(e)
            }

            var r = t.createBrowserStorage("sessionCookies");
            return e.ItemView.extend({
                constructorName: "SubscribeView",
                template: !1,
                ui: {subscribeButton: "#subscribe-button", postStateMessage: ".post-state-msg"},
                events: {"click @ui.subscribeButton": "subscribe"},
                isUserOrEmailKnown: function () {
                    return i.isAuthenticatedUser || i.isIdentifiedUser || i.isRegisteredUser
                },
                subscribe: function () {
                    2 === i.marketChannel || this.isUserOrEmailKnown() ? n() : this.signUp()
                },
                signUp: function () {
                    r.saveItem("isRedirectToSignInPage", "true");
                    var e = window.location.href, t = encodeURIComponent(e);
                    window.location.href = "/user/signin?ckoflag=0&uurl=e3id%3Dredr%26rurl%3D" + t
                }
            }, {
                run: function () {
                    return i.isAuthenticatedUser && "true" === r.readItem("isRedirectToSignInPage") && (r.deleteItem("isRedirectToSignInPage"), n()), new this({el: "#subscribe-box"}).render()
                }
            })
        });
        define('experiments', function () {
            return {
                16356: 1
                ,
                15146: 0
                ,
                27007: 0
                ,
                27887: 0
                ,
                29701: 1
                ,
                24416: 0
                ,
                16191: 1
                ,
                25229: 0
                ,
                26271: 0
                ,
                27125: 0
                ,
                15940: 1
                ,
                30704: 0
                ,
                10895: 0
                ,
                14735: 0
                ,
                16362: 0
                ,
                16125: 0
                ,
                25918: 1
                ,
                15034: 0
                ,
                26566: 0
                ,
                26567: 1
                ,
                24789: 1
                ,
                31748: 0
                ,
                4334: 0
                ,
                27094: 0
                ,
                15762: 0
                ,
                15366: 1
                ,
                15882: 0
                ,
                15881: 0
                ,
                26137: 0
                ,
                25842: 1
                ,
                24510: 0
                ,
                27589: 0
                ,
                24997: 0
                ,
                25162: 0
                ,
                24593: 0
                ,
                15127: 0
                ,
                15521: 1
                ,
                26092: 0
                ,
                13746: 0
                ,
                24807: 0
                ,
                8444: 0
                ,
                15770: 1
                ,
                14044: 1
                ,
                27117: 0
                ,
                26821: 0
                ,
                26303: 0
                ,
                27237: 0
                ,
                26823: 0
                ,
                26701: 0
                ,
                26300: 0
                ,
                16349: 0
                ,
                16346: 1
                ,
                25170: 0
                ,
                16229: 0
                ,
                26518: 0
                ,
                16393: 1
                ,
                14893: 0
                ,
                16431: 1
                ,
                29349: 0
                ,
                15182: 1
                ,
                26877: 0
                ,
                29587: 0
                ,
                24452: 0
                ,
                13168: 0
                ,
                8100: 1
                ,
                15870: 0
                ,
                25679: 1
                ,
                15071: 0
                ,
                27735: 0
                ,
                26481: 0
                ,
                24463: 1
                ,
                25431: 0
                ,
                26123: 0
                ,
                25430: 0
                ,
                15513: 0
                ,
                16206: 0
                ,
                15478: 0
                ,
                30859: 0
                ,
                16324: 0
                ,
                15638: 0
                ,
                26080: 0
                ,
                15879: 0
                ,
                15758: 1
                ,
                15878: 0
                ,
                16013: 0
                ,
                25400: 0
                ,
                24559: 0
                ,
                13543: 0
                ,
                15841: 0
                ,
                15723: 5
                ,
                15327: 0
                ,
                24604: 0
                ,
                16422: 0
                ,
                30707: 0
                ,
                16265: 0
                ,
                26500: 1
                ,
                25653: 0
                ,
                24443: 0
                ,
                27317: 1
                ,
                26065: 0
                ,
                26340: 1
                ,
                28763: 0
                ,
                25772: 0
                ,
                26344: 0
                ,
                28124: 0
                ,
                14764: 0
                ,
                16423: 1
                ,
                15614: 0
            };
        });
        define('serverGroupModel', function () {
            return {};
        });
        define('hotelInfo', ['uitk'], function (uitk) {
            return {
                id: '33204043',
                name: '杭州西湖武林广场亚朵轻居酒店 ',
                city: '杭州',
                cityRegionId: '6084457',
                backToSearchParams: {
                    "endDate": "2019/09/21",
                    "regionId": "6084457",
                    "adults": "2",
                    "destination": "杭州",
                    "vip": "false",
                    "startDate": "2019/09/20"
                },
                goToSearchUrl: "/Hotel-Search?destination=%E6%9D%AD%E5%B7%9E&startDate=2019%2F09%2F20&endDate=2019%2F09%2F21&adults=2&regionId=6084457&vip=false",
                rfrrBase: "HOT.HIS.",
                isDeeplink: true,
                leadPriceResortFeeEnabled: true,
                suppressETP: false,
                dateFormat: '年/月/日',
                maxDate: '2021/01/31',
                langId: '2052',
                locale: 'zh_CN',
                currencyCode: 'CNY',
                currencySymbol: 'CN¥',
                roundCurrency: true,
                ratingCategory: 4,
                regionId: "6084457",
                latLong: "30.26458,120.172739",
                useAlternativeBackToSearchParams: false
            };
        });
        define('userInfo', [], function () {
            'use strict';
            return {
                userTuid: '-1',
                expUserId: '-1',
                siteId: '100001',
                locale: 'zh_CN'
            };
        });
        define('searchData', function () {
            var modelData = {
                "maxRooms": 8,
                "maxAdults": 14,
                "maxChildren": 6,
                "maxChildAge": 17,
                "selRoomIndex": 1,
                "totalAdults": 2,
                "totalChildren": 0,
                "datelessSearch": false,
                "checkIn": "2019/09/20",
                "checkOut": "2019/09/21",
                "checkInDate": "",
                "checkOutDate": "",
                "checkInMedium": "2019/09/20",
                "checkOutMedium": "2019/09/21",
                "minDate": "2019/09/19",
                "maxDate": "2021/01/31",
                "dateRegEx": "^(?:(?:20)*\d\d)[- /.](?:0*[1-9]|1[012])[- /.](?:0*[1-9]|[12][0-9]|3[01])*$",
                "dateFormat": "yyyy/MM/dd",
                "region": {
                    "majorCity": {
                        "province": {
                            "country": {
                                "twoLetterCountryCode": "",
                                "threeLetterCountryCode": "",
                                "id": 6084457,
                                "type": "COUNTRY",
                                "name": " 中国",
                                "latLong": {"latitude": 30.272319, "longitude": 120.136151},
                                "description": "",
                                "isPackageable": false,
                                "airports": [],
                                "equivalentRegions": [],
                                "cityId": 0
                            },
                            "abbreviation": "",
                            "subProvinceName": "",
                            "id": 6084457,
                            "type": "PROVINCESTATE",
                            "name": " 浙江",
                            "latLong": {"latitude": 30.272319, "longitude": 120.136151},
                            "description": "",
                            "isPackageable": false,
                            "airports": [],
                            "equivalentRegions": [],
                            "cityId": 0
                        },
                        "id": 6084457,
                        "type": "MAJORCITY",
                        "name": "杭州",
                        "latLong": {"latitude": 30.272319, "longitude": 120.136151},
                        "description": "",
                        "isPackageable": false,
                        "airports": [],
                        "equivalentRegions": [],
                        "cityId": 0
                    },
                    "id": 6084457,
                    "type": "CITY",
                    "name": "杭州",
                    "latLong": {"latitude": 30.272319, "longitude": 120.136151},
                    "description": "",
                    "isPackageable": false,
                    "airports": [],
                    "equivalentRegions": [],
                    "cityId": 0
                },
                "cityName": "杭州",
                "deeplink": true,
                "rooms": [{"adults": "2", "childAges": []}],
                "checkInISO": "1900-01-01",
                "checkOutISO": "1900-01-01",
                "amenityFilter": [],
                "regionIdSelection": "6084457",
                "vipFilterSelection": "false"
            };
            modelData.shouldShowEDS = true;
            modelData.dateError = false;
            modelData.showSoldOut = false;
            return modelData;
        });
        define('wizardConfig', ['underscore'], function (_) {
            return _.extend({
                "maxRooms": 8,
                "maxAdults": 14,
                "maxChildren": 6,
                "maxChildAge": 17,
                "selRoomIndex": 1,
                "totalAdults": 2,
                "totalChildren": 0,
                "datelessSearch": false,
                "checkIn": "2019/09/20",
                "checkOut": "2019/09/21",
                "checkInDate": "",
                "checkOutDate": "",
                "checkInMedium": "2019/09/20",
                "checkOutMedium": "2019/09/21",
                "minDate": "2019/09/19",
                "maxDate": "2021/01/31",
                "dateRegEx": "^(?:(?:20)*\d\d)[- /.](?:0*[1-9]|1[012])[- /.](?:0*[1-9]|[12][0-9]|3[01])*$",
                "dateFormat": "yyyy/MM/dd",
                "region": {
                    "majorCity": {
                        "province": {
                            "country": {
                                "twoLetterCountryCode": "",
                                "threeLetterCountryCode": "",
                                "id": 6084457,
                                "type": "COUNTRY",
                                "name": " 中国",
                                "latLong": {"latitude": 30.272319, "longitude": 120.136151},
                                "description": "",
                                "isPackageable": false,
                                "airports": [],
                                "equivalentRegions": [],
                                "cityId": 0
                            },
                            "abbreviation": "",
                            "subProvinceName": "",
                            "id": 6084457,
                            "type": "PROVINCESTATE",
                            "name": " 浙江",
                            "latLong": {"latitude": 30.272319, "longitude": 120.136151},
                            "description": "",
                            "isPackageable": false,
                            "airports": [],
                            "equivalentRegions": [],
                            "cityId": 0
                        },
                        "id": 6084457,
                        "type": "MAJORCITY",
                        "name": "杭州",
                        "latLong": {"latitude": 30.272319, "longitude": 120.136151},
                        "description": "",
                        "isPackageable": false,
                        "airports": [],
                        "equivalentRegions": [],
                        "cityId": 0
                    },
                    "id": 6084457,
                    "type": "CITY",
                    "name": "杭州",
                    "latLong": {"latitude": 30.272319, "longitude": 120.136151},
                    "description": "",
                    "isPackageable": false,
                    "airports": [],
                    "equivalentRegions": [],
                    "cityId": 0
                },
                "cityName": "杭州",
                "deeplink": true,
                "rooms": [{"adults": "2", "childAges": []}],
                "checkInISO": "1900-01-01",
                "checkOutISO": "1900-01-01",
                "amenityFilter": [],
                "regionIdSelection": "6084457",
                "vipFilterSelection": "false"
            }, {
                shouldShowEDS: true,
                dateError: false,
                showSoldOut: false,
                dateValidationRegularExpression: /^(?:(?:20)*\d\d)[- /.](?:0*[1-9]|1[012])[- /.](?:0*[1-9]|[12][0-9]|3[01])*$/,
                dateFormat: '年/月/日',
                maximumDateRange: 28
            });
        });
        define('importantAmenityIcons', function () {
            return [
                "freeWifi"
                ,
                "restaurant"
                ,
                "smokeFree"
            ];
        });
        define('reviewsModel', ['infosite'], function (infosite) {
            var reviews = new infosite.DeprecatedModule();
            reviews.tripAdvisorUrl = '//www.tripadvisor.com/api/ratinginfo/1.0/getRating';
            reviews.tripAdvisorRatingsKey = '4cd5d1bc-7d71-4eea-afde-d52f9a1a247c';
            reviews.tripAdvisorKey = 'B14A708F3FB54708A8EDB1168ECF4AB4';
            reviews.showTripAdvisorsWithoutExperiment = 'false';
            reviews.tripAdvisorTrackingImageUrl = '//www.tripadvisor.com/img/cdsi/partner/transparent_pixel-13878-5.gif';
            reviews.ta = {
                locale: 'en'
            };
// Start Experiment 16059
            reviews.isDisplayTopReviewSummary = 'false'
// End Experiment 16059
            reviews.enableTACache = false;
            reviews.reviewsPreloaded = false;
            var reviewsFilterPartUrl = 'categoryFilter=CAT&languageFilter=LNG&searchTerm=SEARCH_TEXT&';
            var reviewsSortPartUrl = 'sortBy=SORT&languageSort=LANGSORT&';
            var reviewsTrackingPartUrl = 'expweb.activityId=3a08e106-326e-43c8-b56b-a9097aff0e86&pageName=page.Hotels.Infosite.Information&origin=&caller=Expedia&guid=c5af0e72-ed39-4922-b542-66aefae94230&translationLocale=LOCALE';
            var url = '/ugc/urs/api/hotelreviews/hotel/HOTELID/?_type=json&start=START_INDEX&items=PER_PAGE&'
                + reviewsFilterPartUrl + reviewsSortPartUrl + reviewsTrackingPartUrl;
            reviews.urs = {
                baseURL: '/ugc/urs/api',
                apiURL: '/ugc/urs/api',
                url: url,
                totalCount: 7,
                perPage: '10',
                pageToLoad: 1,
                paginationToken: '',
                currentSort: '',
                currentCategoryFilter: '',
                currentLanguageFilter: '',
                timeout: 5000,
                langCode: "zh_CN".split('_')[0],
                locale: "zh_CN",
                localeForDate: "zh_CN".replace('_', '-'),
                isVerifiedReviews: true,
                isShowTravellerCkoDate: false,
                languageSortVal: 'zh',
                isShowDetailedReviewsDisclaimer: false,
                loyaltyBrandName: "Expedia Rewards"
            };
            reviews.hotelName = "杭州西湖武林广场亚朵轻居酒店 ";
            reviews.brandName = "Expedia 亿客行";
            reviews.cleanlinessRating = "4.6";
            reviews.cleanlinessSuperlativeMessage = "好极了!";
            reviews.isShowAreaInSqFt = true;
            reviews.isShowGenericReviewSummaryMessaging = false;
            reviews.reviewTranslationEnabled = true;
            reviews.translatableLanguages = 'af,sq,ar,az,eu,bn,be,bg,ca,zh,hr,cs,da,nl,en,eo,et,tl,fi,fr,gl,ka,de,el,gu,ht,he,hi,hu,is,id,ga,it,ja,kn,ko,la,lv,lt,mk,mg,ms,ml,mt,mi,mr,mn,my,ne,nb,fa,pl,pt,ma,ro,ru,sr,st,si,sk,sl,so,es,su,sw,sv,tg,ta,te,th,tr,uk,ur,uz,vi,cy,yi,yo,zu'.split(',');
            reviews.reviewSuperlativeMessage = "好极了!";
            return reviews;
        });
        define('mapConfig', function () {
            'use strict';
            var hotelPinUrl = "//www.expedia.com/static/default/default/images/marker-hotel-6.png",
                poiPinUrl = "//www.expedia.com/static/default/default/images/marker-poi-6.png";
            if (hotelPinUrl != 'red-pin') {
                hotelPinUrl = {url: hotelPinUrl.toString()}
                poiPinUrl = {url: poiPinUrl.toString()}
            }
            return {
                config: {
                    sensor: false,
                    channel: "expedia-HotelInformation",
                    mapApiUrl: "//ditu.google.cn/maps/api/js?v=3&callback=uitk.map.initPlugin",
                    language: 'zh',
                    googleMapEnabled: false,
                    bumiFourSquarePath: 'https://bumi-service.us-west-2.prod.expedia.com/v1/restaurants',
                    tcsPointOfInterestPath: 'https://cs-tcs-services-proxy.prod.expedia.com/ls-locationdisc/service/travel/id/'
                },
                data: {
                    "hotel-map": {
                        "markerData": {
                            "markers": [{
                                "name": " 杭州西湖武林广场亚朵轻居酒店 <div class="star-rating-wrapper">
 <strong class="star-rating rating-secondary star rating" >
 <span class="visuallyhidden">4.0 / 5.0<\/span>
 <span class="icon icon-stars4-0 stars-grey value-title" title="4.0" aria-hidden="true"><\/span>
<\/strong>

 <\/div>

",
                                "latlong": "30.264579999999998705106918350793421268463134765625,120.172739000000007081325748004019260406494140625",
                                "content": " <div class="pushpin-photo">
<figure class="image aspect-ratio1-1" data-media-type="image" data-src="//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/97b8083d_n.jpg" data-aspect-ratio="1-1" data-class="tile-media"><img src="//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/97b8083d_n.jpg" alt="" class="tile-media"/></figure>
 </div>

 <div class="pushpin-address">

<div class="address">
 	<div>
			<span>
	 凤起路 295 号, 下城区, 杭州市, 浙江省
 	</span>
 <span class="phone-number">

 <span itemprop="telephone">
 400 990 1479
 </span>

 </span>
 </div>
</div>
 </div>
",
                                "type": hotelPinUrl
                            }
                                , {
                                    "id": "6222341",
                                    "name": "武林广场",
                                    "latlong": "30.271245,120.163322",
                                    "content": " <ul class="poi-pushpin-content">

 <li>
1.1英里 </li>


 <li>
<span class="icon icon-cars" aria-hidden="true"></span><span class="alt">开车:</span> <span>2分钟</span>
 </li>

 <li>
<span class="icon icon-walk" aria-hidden="true"></span><span class="alt">步行:</span> <span>19分钟</span>
 </li>
 </ul>

",
                                    "type": poiPinUrl
                                }
                                , {
                                    "id": "6232695",
                                    "name": "杭州大厦购物中心",
                                    "latlong": "30.273099,120.161708",
                                    "content": " <ul class="poi-pushpin-content">

 <li>
1.2英里 </li>


 <li>
<span class="icon icon-cars" aria-hidden="true"></span><span class="alt">开车:</span> <span>2分钟</span>
 </li>

 <li>
<span class="icon icon-walk" aria-hidden="true"></span><span class="alt">步行:</span> <span>21分钟</span>
 </li>
 </ul>

",
                                    "type": poiPinUrl
                                }
                                , {
                                    "id": "6233331",
                                    "name": "吴山夜市",
                                    "latlong": "30.252608,120.168362",
                                    "content": " <ul class="poi-pushpin-content">

 <li>
1.3英里 </li>


 <li>
<span class="icon icon-cars" aria-hidden="true"></span><span class="alt">开车:</span> <span>2分钟</span>
 </li>

 <li>
<span class="icon icon-walk" aria-hidden="true"></span><span class="alt">步行:</span> <span>21分钟</span>
 </li>
 </ul>

",
                                    "type": poiPinUrl
                                }
                                , {
                                    "id": "6141424",
                                    "name": "西湖",
                                    "latlong": "30.245538,120.149471",
                                    "content": " <ul class="poi-pushpin-content">

 <li>
1.5英里 </li>


 <li>
<span class="icon icon-cars" aria-hidden="true"></span><span class="alt">开车:</span> <span>3分钟</span>
 </li>

 <li>
<span class="icon icon-walk" aria-hidden="true"></span><span class="alt">步行:</span> <span>26分钟</span>
 </li>
 </ul>

",
                                    "type": poiPinUrl
                                }
                                , {
                                    "id": "6095660",
                                    "name": "断桥",
                                    "latlong": "30.259195,120.15219",
                                    "content": " <ul class="poi-pushpin-content">

 <li>
1.9英里 </li>


 <li>
<span class="icon icon-cars" aria-hidden="true"></span><span class="alt">开车:</span> <span>3分钟</span>
 </li>

 <li>
<span class="icon icon-walk" aria-hidden="true"></span><span class="alt">步行:</span> <span>29分钟</span>
 </li>
 </ul>

",
                                    "type": poiPinUrl
                                }
                                , {
                                    "id": "6095644",
                                    "name": "浙江大学",
                                    "latlong": "30.263947,120.12329",
                                    "content": " <ul class="poi-pushpin-content">

 <li>
3.7英里 </li>


 <li>
<span class="icon icon-cars" aria-hidden="true"></span><span class="alt">开车:</span> <span>6分钟</span>
 </li>

 <li>
<span class="icon icon-walk" aria-hidden="true"></span><span class="alt">步行:</span> <span>68分钟</span>
 </li>
 </ul>

",
                                    "type": poiPinUrl
                                }
                                , {
                                    "id": "6095658",
                                    "name": "杭州植物园",
                                    "latlong": "30.254039,120.123516",
                                    "content": " <ul class="poi-pushpin-content">

 <li>
4.5英里 </li>


 <li>
<span class="icon icon-cars" aria-hidden="true"></span><span class="alt">开车:</span> <span>22分钟</span>
 </li>

 <li>
<span class="icon icon-walk" aria-hidden="true"></span><span class="alt">步行:</span> <span>72分钟</span>
 </li>
 </ul>

",
                                    "type": poiPinUrl
                                }
                                , {
                                    "id": "6095648",
                                    "name": "灵隐寺",
                                    "latlong": "30.24075,120.10154",
                                    "content": " <ul class="poi-pushpin-content">

 <li>
5.5英里 </li>


 <li>
<span class="icon icon-cars" aria-hidden="true"></span><span class="alt">开车:</span> <span>9分钟</span>
 </li>

 <li>
<span class="icon icon-walk" aria-hidden="true"></span><span class="alt">步行:</span> <span>109分钟</span>
 </li>
 </ul>

",
                                    "type": poiPinUrl
                                }
                                , {
                                    "id": "6265485",
                                    "name": "宋城",
                                    "latlong": "30.171127,120.097218",
                                    "content": " <ul class="poi-pushpin-content">

 <li>
9.4英里 </li>


 <li>
<span class="icon icon-cars" aria-hidden="true"></span><span class="alt">开车:</span> <span>14分钟</span>
 </li>

 <li>
<span class="icon icon-walk" aria-hidden="true"></span><span class="alt">步行:</span> <span>少于 2 分钟</span>
 </li>
 </ul>

",
                                    "type": poiPinUrl
                                }
                                , {
                                    "id": "6150574",
                                    "name": "西溪国家湿地公园",
                                    "latlong": "30.270854,120.061426",
                                    "content": " <ul class="poi-pushpin-content">

 <li>
11英里 </li>


 <li>
<span class="icon icon-cars" aria-hidden="true"></span><span class="alt">开车:</span> <span>42分钟</span>
 </li>

 <li>
<span class="icon icon-walk" aria-hidden="true"></span><span class="alt">步行:</span> <span>少于 2 分钟</span>
 </li>
 </ul>

",
                                    "type": poiPinUrl
                                }
                            ]
                        },
                        "customParams": {
                            "center": "30.264579999999998705106918350793421268463134765625,120.172739000000007081325748004019260406494140625",
                            "zoomToFit": false,
                            "title": "	<span class="map-title-with-link">
<a href="javascript:void(0);" class="btn btn-primary btn-text map-close" data-track="HOT.HIS.Map.CloseLink" data-automation="closeMapLink"><span class="btn-label"><span class="icon icon-toggle270" aria-hidden="true"></span><span class="map-heading no-outline">杭州西湖武林广场亚朵轻居酒店 </span></span></a>
 </span>
 <span class="map-title-original">
		杭州西湖武林广场亚朵轻居酒店 
	</span>
 <div class="star-rating-wrapper">
 <strong class="star-rating rating-secondary star rating" >
 <span class="visuallyhidden">4.0 / 5.0</span>
 <span class="icon icon-stars4-0 stars-grey value-title" title="4.0" aria-hidden="true"></span>
</strong>

 </div>
 <div class="map-only-close-button">
<button href="javascript:void(0);" type="button" class="btn-secondary btn-sub-action map-close" data-track="HOT.HIS.Map.OnlyCloseButton" data-automation="closeMap"><span class="btn-label">关闭</span></button>
 </div>
",
                            "subtitle": "
<div class="address">
 	<div>
			<span>
	 凤起路 295 号, 下城区, 杭州市, 浙江省
 	</span>
 <span class="phone-number">

 <span itemprop="telephone">
 400 990 1479
 </span>

 </span>
 </div>
</div>
",
                            "zoom": 14,
                            "legend": true,
                            "legendContent": "
 <h3 id="pointsOfInterest">景点</h3>
 <ul aria-labelledby="pointsOfInterest">
 <li> 武林广场 - 1.1英里
</li>
 <li> 杭州大厦购物中心 - 1.2英里
</li>
 <li> 吴山夜市 - 1.3英里
</li>
 <li> 西湖 - 1.5英里
</li>
 <li> 断桥 - 1.9英里
</li>
 <li> 浙江大学 - 3.7英里
</li>
 <li> 杭州植物园 - 4.5英里
</li>
 <li> 灵隐寺 - 5.5英里
</li>
 <li> 宋城 - 9.4英里
</li>
 <li> 西溪国家湿地公园 - 11英里
</li>
 </ul>



 <h3>最靠近的主要机场:</h3>
 <p>杭州, 中國 (HGH – 蕭山國際機場)</p>

<h3>区域:</h3>
 <p>离杭州西湖武林广场亚朵轻居酒店 最近的大型机场是杭州 (HGH-萧山国际机场) - 25.1 公里/ 15.6 英里。</p>
 <p>距离按照酒店位置到景点或机场的直线距离计算，不一定代表实际的路程距离。</p>
 <p></p>
 <p>显示的距离近似值精确到 0.1 公里或 0.1 英里。</p>

"
                        }
                        , "mapOptions": {
                            "gestureHandling": "greedy"
                            , "zoomControlOptions": {
                                "position": "3"
                            },
                            "streetViewControlOptions": {
                                "position": "3"
                            },
                            "mapTypeControlOptions": {
                                "position": "9"
                            }
                        }
                    }
                },
                "preGeneratedElements": {
                    "reserveButtonBelowMap": " <div class="reserve-button-container below-map">
<button type="button" class="btn-secondary btn-action reserve-button" data-track="HOT.HIS.Map.Reserve.Button" data-automation="reserveButtonMap"><span class="btn-label">预订</span></button>
 </div>
 ",
                    "reserveButtonBelowLegend": " <div class="reserve-button-container below-legend">
<button type="button" class="btn-secondary btn-action reserve-button" data-track="HOT.HIS.Map.Reserve.Button" data-automation="reserveButtonMap"><span class="btn-label">预订</span></button>
 </div>
 "
                }
            };
        });
        define('edsModel', function () {
            return {
                isEdsEnabled: true,
                userTuid: -1
            };
        });
        define('roomsAndRatesData', function () {
            var roomsAndRatePlans = {
                "propertyData": {
                    "bookingFeeMessageEnabled": true,
                    "breakfastChargeAvailable": false,
                    "breakfastIncludedAtProperty": false,
                    "breakfastSurchargeAtProperty": true,
                    "genericFeeMessageEnabled": false,
                    "cleanlinessSuperlativeMessage": null,
                    "internetSurchargeAtProperty": false,
                    "newFreeInternet": true,
                    "suppressETP": false,
                    "vacationRental": false,
                    "goldBranded": "+gold",
                    "silverBranded": "+silver",
                    "ccfeeMessageEnabled": true
                },
                "rooms": {
                    "24-213605642": {
                        "locale": "zh_CN",
                        "roomTypeCode": "213605642",
                        "providerId": "24",
                        "name": "尊贵双床房",
                        "description": ["<p><strong>2 张单人床</strong></p><p>20平方米（215平方尺）</p><br/><p><b>网络</b> - 免费 WiFi </p> <p><b>娱乐</b> - 平板电视带有有线频道</p><p><b>餐饮</b> - 咖啡壶/茶具</p><p><b>浴室</b> - 私人浴室备有淋浴、浴衣和吹风机</p><p><b>舒适设施/服务</b> - 恒温控制空调</p><p>无烟客房</p>&nbsp;"],
                        "photos": [{
                            "thumbnailUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/84feaa42_n.jpg",
                            "largeUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/84feaa42_l.jpg",
                            "large1000Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/84feaa42_z.jpg",
                            "large500Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/84feaa42_y.jpg",
                            "bigUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/84feaa42_b.jpg",
                            "caption": "",
                            "displayText": "客房"
                        }, {
                            "thumbnailUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/d3ada91a_n.jpg",
                            "largeUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/d3ada91a_l.jpg",
                            "large1000Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/d3ada91a_z.jpg",
                            "large500Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/d3ada91a_y.jpg",
                            "bigUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/d3ada91a_b.jpg",
                            "caption": "",
                            "displayText": "客房"
                        }, {
                            "thumbnailUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/ac8c6c82_n.jpg",
                            "largeUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/ac8c6c82_l.jpg",
                            "large1000Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/ac8c6c82_z.jpg",
                            "large500Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/ac8c6c82_y.jpg",
                            "bigUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/ac8c6c82_b.jpg",
                            "caption": "",
                            "displayText": "客房"
                        }, {
                            "thumbnailUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/cb4f3c4f_n.jpg",
                            "largeUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/cb4f3c4f_l.jpg",
                            "large1000Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/cb4f3c4f_z.jpg",
                            "large500Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/cb4f3c4f_y.jpg",
                            "bigUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/cb4f3c4f_b.jpg",
                            "caption": "",
                            "displayText": "客房"
                        }, {
                            "thumbnailUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b9c6ccb7_n.jpg",
                            "largeUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b9c6ccb7_l.jpg",
                            "large1000Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b9c6ccb7_z.jpg",
                            "large500Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b9c6ccb7_y.jpg",
                            "bigUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b9c6ccb7_b.jpg",
                            "caption": "",
                            "displayText": "客房服务设施"
                        }],
"],
                        "roomSquareFeet": "215",
                        "roomSquareMeters": "20",
                        "hasRoomView": false,
                        "amenities": {
                            "2403": "免费 WiFi",
                            "132": "泡咖啡/茶用具",
                            "361": "提供早餐（收费）",
                            "9": "健身设施",
                            "141": "私人浴室",
                            "2030": "房内恒温控制（空调）",
                            "142": "浴袍",
                            "144": "吹风机",
                            "19": "餐厅",
                            "52": "房间总数 -",
                            "2166": "只提供淋浴",
                            "2390": "免费 WiFi",
                            "2137": "无烟酒店",
                            "2398": "有线电视服务",
                            "2399": "平板电视"
                        },
                        "maxChildren": 2,
                        "maxGuests": 4,
                        "extraBedNames": [],
                        "cribBedding": null,
                        "rollawayBedding": null,
                        "extraBeddingOptions": null,
                        "cribBeddingAndRollawayBedding": null,
                        "hasBedNames": true,
                        "ratePlans": [],
                        "rewardsPoints": 0,
                        "maxOccupancyValid": true,
                        "bedsAndRoomOccupancyInfo": {
                            "maxRoomOcc": {"total": 4, "children": 2, "adults": 2},
                            "recommendedRoomOcc": {"total": 2, "children": 1, "adults": 2},
                            "extraBed": [{"type": "", "size": "", "quantity": 0, "name": ""}],
                            "bedGroups": [{
                                "id": "37341",
                                "name": "2 张单人床",
                                "bedTypes": [{
                                    "type": "单人床",
                                    "size": {"minWidth": 74, "maxWidth": 100, "sizeUnit": "CM"},
                                    "occupancy": {"total": 1, "children": 1, "adults": 1}
                                }]
                            }]
                        },
                        "bedNames": ["2 张单人床"]
                    },
                    "24-213605641": {
                        "locale": "zh_CN",
                        "roomTypeCode": "213605641",
                        "providerId": "24",
                        "name": "特级双床房",
                        "description": ["<p><strong>2 张单人床</strong></p><p>20平方米（215平方尺）</p><br/><p><b>网络</b> - 免费 WiFi </p> <p><b>娱乐</b> - 平板电视带有有线频道</p><p><b>餐饮</b> - 咖啡壶/茶具</p><p><b>浴室</b> - 私人浴室备有淋浴、浴衣和吹风机</p><p><b>舒适设施/服务</b> - 恒温控制空调</p><p>无烟客房</p>&nbsp;"],
                        "photos": [{
                            "thumbnailUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/84feaa42_n.jpg",
                            "largeUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/84feaa42_l.jpg",
                            "large1000Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/84feaa42_z.jpg",
                            "large500Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/84feaa42_y.jpg",
                            "bigUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/84feaa42_b.jpg",
                            "caption": "",
                            "displayText": "客房"
                        }, {
                            "thumbnailUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/d3ada91a_n.jpg",
                            "largeUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/d3ada91a_l.jpg",
                            "large1000Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/d3ada91a_z.jpg",
                            "large500Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/d3ada91a_y.jpg",
                            "bigUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/d3ada91a_b.jpg",
                            "caption": "",
                            "displayText": "客房"
                        }, {
                            "thumbnailUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/ac8c6c82_n.jpg",
                            "largeUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/ac8c6c82_l.jpg",
                            "large1000Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/ac8c6c82_z.jpg",
                            "large500Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/ac8c6c82_y.jpg",
                            "bigUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/ac8c6c82_b.jpg",
                            "caption": "",
                            "displayText": "客房"
                        }, {
                            "thumbnailUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/cb4f3c4f_n.jpg",
                            "largeUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/cb4f3c4f_l.jpg",
                            "large1000Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/cb4f3c4f_z.jpg",
                            "large500Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/cb4f3c4f_y.jpg",
                            "bigUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/cb4f3c4f_b.jpg",
                            "caption": "",
                            "displayText": "客房"
                        }, {
                            "thumbnailUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b9c6ccb7_n.jpg",
                            "largeUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b9c6ccb7_l.jpg",
                            "large1000Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b9c6ccb7_z.jpg",
                            "large500Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b9c6ccb7_y.jpg",
                            "bigUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b9c6ccb7_b.jpg",
                            "caption": "",
                            "displayText": "客房服务设施"
                        }],
"],
                        "roomSquareFeet": "215",
                        "roomSquareMeters": "20",
                        "hasRoomView": false,
                        "amenities": {
                            "2403": "免费 WiFi",
                            "132": "泡咖啡/茶用具",
                            "361": "提供早餐（收费）",
                            "9": "健身设施",
                            "141": "私人浴室",
                            "2030": "房内恒温控制（空调）",
                            "142": "浴袍",
                            "144": "吹风机",
                            "19": "餐厅",
                            "52": "房间总数 -",
                            "2166": "只提供淋浴",
                            "2390": "免费 WiFi",
                            "2137": "无烟酒店",
                            "2398": "有线电视服务",
                            "2399": "平板电视"
                        },
                        "maxChildren": 2,
                        "maxGuests": 4,
                        "extraBedNames": [],
                        "cribBedding": null,
                        "rollawayBedding": null,
                        "extraBeddingOptions": null,
                        "cribBeddingAndRollawayBedding": null,
                        "hasBedNames": true,
                        "ratePlans": [],
                        "rewardsPoints": 0,
                        "maxOccupancyValid": true,
                        "bedsAndRoomOccupancyInfo": {
                            "maxRoomOcc": {"total": 4, "children": 2, "adults": 2},
                            "recommendedRoomOcc": {"total": 2, "children": 1, "adults": 2},
                            "extraBed": [{"type": "", "size": "", "quantity": 0, "name": ""}],
                            "bedGroups": [{
                                "id": "37341",
                                "name": "2 张单人床",
                                "bedTypes": [{
                                    "type": "单人床",
                                    "size": {"minWidth": 74, "maxWidth": 100, "sizeUnit": "CM"},
                                    "occupancy": {"total": 1, "children": 1, "adults": 1}
                                }]
                            }]
                        },
                        "bedNames": ["2 张单人床"]
                    },
                    "24-213605640": {
                        "locale": "zh_CN",
                        "roomTypeCode": "213605640",
                        "providerId": "24",
                        "name": "尊贵客房",
                        "description": ["<p><strong>1 张特大床</strong></p><p>20平方米（215平方尺）</p><br/><p><b>网络</b> - 免费 WiFi </p> <p><b>娱乐</b> - 平板电视带有有线频道</p><p><b>餐饮</b> - 咖啡壶/茶具</p><p><b>浴室</b> - 私人浴室备有淋浴、浴衣和吹风机</p><p><b>舒适设施/服务</b> - 恒温控制空调</p><p>无烟客房</p>&nbsp;"],
                        "photos": [{
                            "thumbnailUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/2d95cb18_n.jpg",
                            "largeUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/2d95cb18_l.jpg",
                            "large1000Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/2d95cb18_z.jpg",
                            "large500Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/2d95cb18_y.jpg",
                            "bigUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/2d95cb18_b.jpg",
                            "caption": "",
                            "displayText": "客房"
                        }, {
                            "thumbnailUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/84c5e491_n.jpg",
                            "largeUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/84c5e491_l.jpg",
                            "large1000Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/84c5e491_z.jpg",
                            "large500Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/84c5e491_y.jpg",
                            "bigUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/84c5e491_b.jpg",
                            "caption": "",
                            "displayText": "客房"
                        }, {
                            "thumbnailUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b4acd68b_n.jpg",
                            "largeUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b4acd68b_l.jpg",
                            "large1000Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b4acd68b_z.jpg",
                            "large500Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b4acd68b_y.jpg",
                            "bigUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b4acd68b_b.jpg",
                            "caption": "",
                            "displayText": "客房"
                        }, {
                            "thumbnailUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/92e71113_n.jpg",
                            "largeUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/92e71113_l.jpg",
                            "large1000Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/92e71113_z.jpg",
                            "large500Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/92e71113_y.jpg",
                            "bigUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/92e71113_b.jpg",
                            "caption": "",
                            "displayText": "起居区"
                        }, {
                            "thumbnailUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b9c6ccb7_n.jpg",
                            "largeUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b9c6ccb7_l.jpg",
                            "large1000Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b9c6ccb7_z.jpg",
                            "large500Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b9c6ccb7_y.jpg",
                            "bigUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b9c6ccb7_b.jpg",
                            "caption": "",
                            "displayText": "客房服务设施"
                        }],
"],
                        "roomSquareFeet": "215",
                        "roomSquareMeters": "20",
                        "hasRoomView": false,
                        "amenities": {
                            "2403": "免费 WiFi",
                            "132": "泡咖啡/茶用具",
                            "361": "提供早餐（收费）",
                            "9": "健身设施",
                            "141": "私人浴室",
                            "2030": "房内恒温控制（空调）",
                            "142": "浴袍",
                            "144": "吹风机",
                            "19": "餐厅",
                            "52": "房间总数 -",
                            "2166": "只提供淋浴",
                            "2390": "免费 WiFi",
                            "2137": "无烟酒店",
                            "2398": "有线电视服务",
                            "2399": "平板电视"
                        },
                        "maxChildren": 2,
                        "maxGuests": 4,
                        "extraBedNames": [],
                        "cribBedding": null,
                        "rollawayBedding": null,
                        "extraBeddingOptions": null,
                        "cribBeddingAndRollawayBedding": null,
                        "hasBedNames": true,
                        "ratePlans": [],
                        "rewardsPoints": 0,
                        "maxOccupancyValid": true,
                        "bedsAndRoomOccupancyInfo": {
                            "maxRoomOcc": {"total": 4, "children": 2, "adults": 2},
                            "recommendedRoomOcc": {"total": 3, "children": 2, "adults": 2},
                            "extraBed": [{"type": "", "size": "", "quantity": 0, "name": ""}],
                            "bedGroups": [{
                                "id": "37321",
                                "name": "1 张特大床",
                                "bedTypes": [{
                                    "type": "特大床",
                                    "size": {"minWidth": 180, "maxWidth": 210, "sizeUnit": "CM"},
                                    "occupancy": {"total": 3, "children": 3, "adults": 2}
                                }]
                            }]
                        },
                        "bedNames": ["1 张特大床"]
                    },
                    "24-213605639": {
                        "locale": "zh_CN",
                        "roomTypeCode": "213605639",
                        "providerId": "24",
                        "name": "客房",
                        "description": ["<p><strong>1 张大床</strong></p><p>20平方米（215平方尺）</p><br/><p><b>网络</b> - 免费 WiFi </p> <p><b>娱乐</b> - 平板电视带有有线频道</p><p><b>餐饮</b> - 咖啡壶/茶具</p><p><b>浴室</b> - 私人浴室备有淋浴、浴衣和吹风机</p><p><b>舒适设施/服务</b> - 恒温控制空调</p><p>无烟客房</p>&nbsp;"],
                        "photos": [{
                            "thumbnailUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/2d95cb18_n.jpg",
                            "largeUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/2d95cb18_l.jpg",
                            "large1000Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/2d95cb18_z.jpg",
                            "large500Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/2d95cb18_y.jpg",
                            "bigUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/2d95cb18_b.jpg",
                            "caption": "",
                            "displayText": "客房"
                        }, {
                            "thumbnailUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/84c5e491_n.jpg",
                            "largeUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/84c5e491_l.jpg",
                            "large1000Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/84c5e491_z.jpg",
                            "large500Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/84c5e491_y.jpg",
                            "bigUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/84c5e491_b.jpg",
                            "caption": "",
                            "displayText": "客房"
                        }, {
                            "thumbnailUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b4acd68b_n.jpg",
                            "largeUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b4acd68b_l.jpg",
                            "large1000Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b4acd68b_z.jpg",
                            "large500Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b4acd68b_y.jpg",
                            "bigUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b4acd68b_b.jpg",
                            "caption": "",
                            "displayText": "客房"
                        }, {
                            "thumbnailUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/92e71113_n.jpg",
                            "largeUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/92e71113_l.jpg",
                            "large1000Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/92e71113_z.jpg",
                            "large500Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/92e71113_y.jpg",
                            "bigUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/92e71113_b.jpg",
                            "caption": "",
                            "displayText": "起居区"
                        }, {
                            "thumbnailUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b9c6ccb7_n.jpg",
                            "largeUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b9c6ccb7_l.jpg",
                            "large1000Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b9c6ccb7_z.jpg",
                            "large500Url": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b9c6ccb7_y.jpg",
                            "bigUrl": "//images.trvl-media.com/hotels/34000000/33210000/33204100/33204043/b9c6ccb7_b.jpg",
                            "caption": "",
                            "displayText": "客房服务设施"
                        }],
"],
                        "roomSquareFeet": "215",
                        "roomSquareMeters": "20",
                        "hasRoomView": false,
                        "amenities": {
                            "2403": "免费 WiFi",
                            "132": "泡咖啡/茶用具",
                            "361": "提供早餐（收费）",
                            "9": "健身设施",
                            "141": "私人浴室",
                            "2030": "房内恒温控制（空调）",
                            "142": "浴袍",
                            "144": "吹风机",
                            "19": "餐厅",
                            "52": "房间总数 -",
                            "2166": "只提供淋浴",
                            "2390": "免费 WiFi",
                            "2137": "无烟酒店",
                            "2398": "有线电视服务",
                            "2399": "平板电视"
                        },
                        "maxChildren": 2,
                        "maxGuests": 4,
                        "extraBedNames": [],
                        "cribBedding": null,
                        "rollawayBedding": null,
                        "extraBeddingOptions": null,
                        "cribBeddingAndRollawayBedding": null,
                        "hasBedNames": true,
                        "ratePlans": [],
                        "rewardsPoints": 0,
                        "maxOccupancyValid": true,
                        "bedsAndRoomOccupancyInfo": {
                            "maxRoomOcc": {"total": 4, "children": 2, "adults": 2},
                            "recommendedRoomOcc": {"total": 2, "children": 1, "adults": 2},
                            "extraBed": [{"type": "", "size": "", "quantity": 0, "name": ""}],
                            "bedGroups": [{
                                "id": "37310",
                                "name": "1 张大床",
                                "bedTypes": [{
                                    "type": "大床",
                                    "size": {"minWidth": 150, "maxWidth": 180, "sizeUnit": "CM"},
                                    "occupancy": {"total": 2, "children": 2, "adults": 2}
                                }]
                            }]
                        },
                        "bedNames": ["1 张大床"]
                    }
                },
                "ratePlans": {}
            };
            return {
                rooms: roomsAndRatePlans.rooms
"""
if 'infosite.offersData' in str_data:
    print('进入offersData....')
    regex = re.compile(r'infosite\.offersData(.*?)roomsAndRatePlans\.rooms', re.S)
    str_data1 = regex.findall(str_data)
    # print(str_data1)
    if len(str_data1) > 0:
        print('.............')
        str_data = str_data1[0]
    # print(str_data)
    regex1 = re.compile(r'"roomTypeCode":.*?"(.*?)".*?"name":.*?"(.*?)"', re.S)
    resp1 = regex1.findall(str_data)  # 房子类型
    print(resp1)
    regex2 = re.compile(r'"hotelID".*?"roomTypeCode": "(.*?)".*?"displayPrice": "(.*?)"', re.S)
    # regex2 = re.compile(r'"hotelID":.*?"roomTypeCode":.*?"(.*?)".*?"displayPrice":.*?"(.*?)"', re.S)
    resp2 = regex2.findall(str_data)  # 房子价格
    print(resp2)
    # resp_dict = dict()
    # for tuple_data in resp2:
    #     if tuple_data[0] not in resp_dict.keys():
    #         resp_dict[tuple_data[0]] = tuple_data[1]
    # for resp_data in resp1:
    #     house_num = resp_data[0]
    #     house_price = resp_dict.get(house_num, '')
    #     house_name = resp_data[1]
    #     if house_price and '房' in house_name:
    #         print(house_name, house_price)

#         else:
#             pass
#             # print(house_num, resp_data[1], '无价格!!!')
# else:
#     print('进入无offersData....')
#     regex = re.compile(r'"roomTypeCode":.*?".*?".*?"name":.*?"(.*?)".*?"displayPrice":.*?"(.*?)"', re.S)
#     resp = regex.findall(str_data)  # 房子类型
#     for resp_data in resp:
#         house_name = resp_data[0]
#         house_price = resp_data[1]
#         print(house_name, house_price)

