public class Swapper
{
    public object[] Arguments { get; private set; }
    
    public Swapper(object[] args)
    {
        Arguments = args;
    }
    
    public void SwapValues()
    {
        object[] args = this.Arguments;
        
        object temp = args[0];
        args[0] = args[1];
        args[1] = temp;
    }
}