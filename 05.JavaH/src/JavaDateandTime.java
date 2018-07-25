import java.time.format.DateTimeFormatter;
import java.util.Calendar;
import java.util.Scanner;

public class JavaDateandTime {

    public static String getDay(String day, String month, String year) {
        int iDay = Integer.parseInt(day);
        int iMonth = Integer.parseInt(month);
        int iYear = Integer.parseInt(year);

        Calendar cal = Calendar.getInstance();
        cal.set(Calendar.DAY_OF_MONTH, iDay);
        cal.set(Calendar.MONTH, iMonth - 1);
        cal.set(Calendar.YEAR, iYear);

        int dayOfWeek = cal.get(Calendar.DAY_OF_WEEK);
        System.out.println(dayOfWeek);
        if (dayOfWeek == Calendar.SUNDAY) {
            return "SUNDAY";
        }
        else if (dayOfWeek == Calendar.MONDAY) {
            return "MONDAY";
        }
        else if (dayOfWeek == Calendar.TUESDAY) {
            return "TUESDAY";
        }
        else if (dayOfWeek == Calendar.WEDNESDAY) {
            return "WEDNESDAY";
        }
        else if (dayOfWeek == Calendar.THURSDAY) {
            return "THURSDAY";
        }
        else if (dayOfWeek == Calendar.FRIDAY) {
            return "FRIDAY";
        }
        else {
            return "SATURDAY";
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String month = in.next();
        String day = in.next();
        String year = in.next();

        System.out.println(getDay(day, month, year));
    }

}
