# டெஸ்ட் ரயில்

## __முன்னுரை__

        டெஸ்ட் ரயில்  ஒரு வலையதள மென்பொருள். இந்த மென்பொருளை வைத்து  கையேடு பரிசோதனை 
    மற்றும்  தன்னியக்க  பரிசோதனை செய்யலாம்.உலகின் மிக பெரிய நிறுவனங்கள் 
    இதை பயன்படுத்துகின்றனர். 
        மேலும் டெஸ்ட் ரயில் பற்றிய தகவலுக்கு http://www.gurock.com/testrail/  வலயத்தளத்தை  பார்க்கவும்.
    இந்த மென்பொருள் பயன்பாடு பைதான் வைத்து உருவாக்கப்பட்டுள்ளது. 
    இந்த பயன்பாடு பரிசோதனைக்கு பைத்தானின் பைடெஸ்ட் உபயோகப்படுத்தப்பட்டுள்ளது

## செயல்முறை
    இந்த  பயன்பாடு அமைப்புக்கு மேகக்கணி தரவு அல்லது சேவையகம் ( சர்வர் ) மூலமாக பயன்படுத்தலாம். 
    நான் மேகக்கணி பயன்படுத்தி இந்த பயன்பாட்டை  உருவாக்கியுள்ளேன்.

### டெஸ்ட் ரயில் மேகக்கணி அமைப்பு
https://secure.gurock.com/customers/testrail/trial/  வலயத்தளத்தில் சென்று டெஸ்ட் ரயில் கிளவுட் 
என்ற விருப்பத்தைதேர்வு செய்யவும்.ட்ரயல்  பிரிவில் உங்களுடைய  விருப்பத்தை உள்ளீடவும்


### Alt-H1  ரயில் சேவையக அமைப்பு
டெஸ்ட் ரயில் சேவையகத்தை  வலயத்தளத்தில்  இருந்து பதிவிறக்கம் செய்யவும்
http://docs.gurock.com/testrail-admin/installation-windows அல்லது 
http://docs.gurock.com/testrail-admin/installation-unix வலயத்தளத்தில் கொடுக்கப்பட்டுள்ள 
செயல்முறையை பின்பற்றி, சேவையகத்தை  அமைவடிமம்   செய்யவும்


## பரிசோதனை
TestRailHelper.py கோப்பில் TestTRHelper  கிளாஸ்சில் சோதனைகள் உள்ளது . இதை பயன்படுத்த
கட்டளை வரியில் pytest -s TestRailHelper.py என்று  உள்ளீடவும்

