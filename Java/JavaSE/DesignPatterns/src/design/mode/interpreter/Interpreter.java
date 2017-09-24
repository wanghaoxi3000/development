package design.mode.interpreter;

import java.util.LinkedList;
import java.util.List;

/**
 * Created by whx3000 on 2017/4/11
 * you can contact me at: wanghaoxi3000@163.com
 */

//Context, 包含解释器之外的一些全局信息
class Context {
    private String input;

    public String getInput() {
        return input;
    }

    public void setInput(String input) {
        this.input = input;
    }

    private String output;

    public String getOutput() {
        return output;
    }

    public void setOutput(String output) {
        this.output = output;
    }
}

//抽象表达式, 声明一个抽象的解释操作, 这个接口为抽象语法树中所有节点共享
abstract class AbstractExpression
{
    public abstract void Interpret(Context context);
}

//终端表达式, 实现与文法中终结符相关联的解释操作. 实现抽象表达式中所要求的接口
//文法中每一个终结符都有一个具体的终结表达式与之对应
class TerminalExpression extends AbstractExpression {
    @Override
    public void Interpret(Context context) {
        System.out.printf("终端解释器");
    }
}

//为文法中的非终结符实现解释操作.
class NonterminalExpression extends AbstractExpression {
    @Override
    public void Interpret(Context context) {
        System.out.println("非终端解释器");
    }
}

//构建表示该文法定义的语言中一个特定的句子的抽象语法树. 调用解释操作.
public class Interpreter {
    public static void main(String args[]) {
        Context context = new Context();
        List<AbstractExpression> list = new LinkedList<>();
        list.add(new TerminalExpression());
        list.add(new NonterminalExpression());
        list.add(new TerminalExpression());
        list.add(new TerminalExpression());

        for(AbstractExpression exp: list) {
            exp.Interpret(context);
        }
    }
}
