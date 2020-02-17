// https://www.reddit.com/r/thinkpad/comments/7n8eyu/thinkpad_led_control_under_gnulinux/

#include <iostream>
#include <cstdlib>

const char * EC_SYS_ENABLE_STR       = "sudo modprobe -r ec_sys";
const char * EC_SYS_ENABLE_WRITE_STR = "sudo modprobe ec_sys write_support=1";

const char * POWER_BUTTON_ON_STR    = "echo \"0 on\" | tee /proc/acpi/ibm/led 1> /dev/null";
const char * POWER_BUTTON_OFF_STR   = "echo \"0 off\" | tee /proc/acpi/ibm/led 1> /dev/null";
const char * POWER_BUTTON_BLINK_STR = "echo \"0 blink\" | tee /proc/acpi/ibm/led 1> /dev/null";

// \x means hexidecimal
// first digit means off/on/blink
// second digit indicates which LED
// a = red led on back, 0 = power, 6 = Fn lock, 7 = sleep, e = microphone
const char * BACK_LED_ON_STR    = "echo -n \"\x8a\" | sudo dd of=\"/sys/kernel/debug/ec/ec0/io\" bs=1 seek=12 count=1 conv=notrunc 2> /dev/null";
const char * BACK_LED_OFF_STR   = "echo -n \"\x0a\" | sudo dd of=\"/sys/kernel/debug/ec/ec0/io\" bs=1 seek=12 count=1 conv=notrunc 2> /dev/null";
const char * BACK_LED_BLINK_STR = "echo -n \"\xca\" | sudo dd of=\"/sys/kernel/debug/ec/ec0/io\" bs=1 seek=12 count=1 conv=notrunc 2> /dev/null";

const char * FN_LED_ON_STR    = "echo -n \"\x86\" | sudo dd of=\"/sys/kernel/debug/ec/ec0/io\" bs=1 seek=12 count=1 conv=notrunc 2> /dev/null";
const char * FN_LED_OFF_STR   = "echo -n \"\x06\" | sudo dd of=\"/sys/kernel/debug/ec/ec0/io\" bs=1 seek=12 count=1 conv=notrunc 2> /dev/null";
const char * FN_LED_BLINK_STR = "echo -n \"\xc6\" | sudo dd of=\"/sys/kernel/debug/ec/ec0/io\" bs=1 seek=12 count=1 conv=notrunc 2> /dev/null";

const char * MIC_LED_ON_STR    = "echo -n \"\x8e\" | sudo dd of=\"/sys/kernel/debug/ec/ec0/io\" bs=1 seek=12 count=1 conv=notrunc 2> /dev/null";
const char * MIC_LED_OFF_STR   = "echo -n \"\x0e\" | sudo dd of=\"/sys/kernel/debug/ec/ec0/io\" bs=1 seek=12 count=1 conv=notrunc 2> /dev/null";
const char * MIC_LED_BLINK_STR = "echo -n \"\xce\" | sudo dd of=\"/sys/kernel/debug/ec/ec0/io\" bs=1 seek=12 count=1 conv=notrunc 2> /dev/null";


void init(){
    std::cout << "init" << std::endl;
    system(EC_SYS_ENABLE_STR);
    system(EC_SYS_ENABLE_WRITE_STR);
    return;
}

void back_led_blink(){
    std::cout << "back_led_blink" << std::endl;
    system(BACK_LED_BLINK_STR);
    return;
}

void back_led_off(){
    std::cout << "back_led_off" << std::endl;
    system(BACK_LED_OFF_STR);
    return;
}

void back_led_on(){
    std::cout << "back_led_on" << std::endl;
    system(BACK_LED_ON_STR);
    return;
}

void fn_led_blink(){
    std::cout << "fn_led_blink" << std::endl;
    system(FN_LED_BLINK_STR);
    return;
}

void fn_led_off(){
    std::cout << "fn_led_off" << std::endl;
    system(FN_LED_OFF_STR);
    return;
}

void fn_led_on(){
    std::cout << "fn_led_on" << std::endl;
    system(FN_LED_ON_STR);
    return;
}

void mic_led_blink(){
    std::cout << "mic_led_blink" << std::endl;
    system(MIC_LED_BLINK_STR);
    return;
}

void mic_led_off(){
    std::cout << "mic_led_off" << std::endl;
    system(MIC_LED_OFF_STR);
    return;
}

void mic_led_on(){
    std::cout << "mic_led_on" << std::endl;
    system(MIC_LED_ON_STR);
    return;
}

void power_button_blink(){
    std::cout << "power_button_blink" << std::endl;
    system(POWER_BUTTON_BLINK_STR);
    return;
}

void power_button_off(){
    std::cout << "power_button_off" << std::endl;
    system(POWER_BUTTON_OFF_STR);
    return;
}

void power_button_on(){
    std::cout << "power_button_on" << std::endl;
    system(POWER_BUTTON_ON_STR);
    return;
}

int main(){

    init();

    back_led_blink();
    system("sleep 2");
    back_led_off();
    system("sleep 2");
    back_led_on();
    system("sleep 2");

    fn_led_blink();
    system("sleep 2");
    fn_led_on();
    system("sleep 2");
    fn_led_off();
    system("sleep 2");

    mic_led_blink();
    system("sleep 2");
    mic_led_on();
    system("sleep 2");
    mic_led_off();
    system("sleep 2");

    power_button_blink();
    system("sleep 2");
    power_button_off();
    system("sleep 2");
    power_button_on();
    system("sleep 2");

    return 0;
}
