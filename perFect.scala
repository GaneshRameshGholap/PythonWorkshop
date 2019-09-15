import scala.io.StdIn._
import scala.util._
class Perfect
{
      var sum:Int=0;
      def checkPerfect(x:Int)
      {
           for(i<-1 until x)
           {
                if(x%i==0)
               {
                  sum=sum+i;    
               }
           }
           if(sum==x)
             println("Perfect Number:");
           else
             println("Not Perfect Number");
      }
}
object perFect
{
   def main(args:Array[String])
   {
         println("Enter the value of n:");
          var n1:Int=readInt();
         var n=scala.util.Random;
         var ob=new Perfect();
         for(i<-1 to n1)
         {
                  var n2=n.nextInt(100);
                  println("Number="+n2);
                  ob.checkPerfect(n2);
         }    
   }
}