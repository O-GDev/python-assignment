    import java.util.Scanner;

    public class PizzaOrderingApp {

        public static void main(String[] args) {

            String priceTable =
                    "----------------------------------------------------\n" +
                    "|Pizza Type   |Number of Slices   |Price Per Box   |\n" +
                    "----------------------------------------------------\n" +
                    "|Sapa Size    |4                  |2,000           |\n" +
                    "----------------------------------------------------\n" +
                    "|Small Money  |6                  |2,400           |\n" +
                    "----------------------------------------------------\n" +
                    "|Big Boys     |8                  |3,000           |\n" +
                    "----------------------------------------------------\n" +
                    "|Odogwu       |12                 |4,200           |\n" +
                    "----------------------------------------------------";

            System.out.println(priceTable);

            Scanner input = new Scanner(System.in);

            System.out.print("Enter the number of people: ");
            int numberOfPeople = input.nextInt();
            input.nextLine();

            System.out.print("What type of pizza do you want?: ");
            String pizzaType = input.nextLine().toLowerCase();

            int numberOfBoxesToBuy = 0;
            int leftOver = 0;
            int customerCost = 0;
            int overallSlices = 0;
            int price = 0;


            if (pizzaType.equals("sapa size")) {
                price = 2000;
                numberOfBoxesToBuy = numberOfPeople / 4;
                if (numberOfPeople % 4 != 0) {
                    numberOfBoxesToBuy += 1;
                    leftOver = 4 - (numberOfPeople % 4);
                }
                customerCost = numberOfBoxesToBuy * price;
                overallSlices = numberOfBoxesToBuy * 4;
            }
            if (pizzaType.equals("small money")) {
                price = 2400;
                numberOfBoxesToBuy = numberOfPeople / 6;
                if (numberOfPeople % 6 != 0) {
                    numberOfBoxesToBuy += 1;
                    leftOver = 6 - (numberOfPeople % 6);
                }
                customerCost = numberOfBoxesToBuy * price;
                overallSlices = numberOfBoxesToBuy * 6;
            }
            if (pizzaType.equals("big boys")) {
                price = 3000;
                numberOfBoxesToBuy = numberOfPeople / 8;
                if (numberOfPeople % 8 != 0) {
                    numberOfBoxesToBuy += 1;
                    leftOver = 8 - (numberOfPeople % 8);
                }
                customerCost = numberOfBoxesToBuy * price;
                overallSlices = numberOfBoxesToBuy * 8;
            }
            if (pizzaType.equals("odogwu")) {
                price = 4200;
                numberOfBoxesToBuy = numberOfPeople / 12;
                if (numberOfPeople % 12 != 0) {
                    numberOfBoxesToBuy += 1;
                    leftOver = 12 - (numberOfPeople % 12);
                }
                customerCost = numberOfBoxesToBuy * price;
                overallSlices = numberOfBoxesToBuy * 12;
            }
else{
        System.out.print("Invalid input!");
    }

            
        
            System.out.println("Number of boxes of pizza to buy = " + numberOfBoxesToBuy + " boxes (explanation: " + pizzaType + " contains " + numberOfBoxesToBuy + " boxes are enough for " + numberOfPeople + " people as they contain " + overallSlices + " total slices).");

            System.out.println("Number of leftover slices = " + leftOver + " slices (explanation: After serving " + numberOfPeople + " people, you will have " + leftOver + " slices left).");

            System.out.println("Price = " + customerCost + " (explanation: " + price + " per box × " + numberOfBoxesToBuy + " boxes).");
        }
    }

