from antlr4 import *
# pip install antlr4-python3-runtime

from gen.throwListener import throwListener
from gen.throwVisitor import *

# pip install antlr4-python3-runtime


class Mylistener(throwListener):
    def __init__(self):
        self.field_list = []
        self.field_list_2 = []
    def enterId2(self, ctx:throwParser.Id2Context):
        self.field_list.append(ctx.getText())
    def enterId4(self, ctx:throwParser.Id4Context):
        self.field_list_2.append(ctx.getText())
    # # DFS
    # def enterCompilationUnit(self, ctx:JavaParserLabeled.CompilationUnitContext):
    #     print("I enterned compilation Unit.")
    #
    # def exitCompilationUnit(self, ctx:JavaParserLabeled.CompilationUnitContext):
    #     print("I exited compilation Unit.")
    #
    # def enterClassDeclaration(self, ctx:JavaParserLabeled.ClassDeclarationContext):
    #     print("Enter Class Decleration")
    #     print(ctx.IDENTIFIER())
    #     print(ctx.CLASS())
    #     print(ctx.classBody().getText())
    #
    # def exitClassDeclaration(self, ctx:JavaParserLabeled.ClassDeclarationContext):
    #     print("Exit Class Decleration")
    #
    # def exitMethodDeclaration(self, ctx:JavaParserLabeled.MethodDeclarationContext):
    #     print(ctx.IDENTIFIER())    ## printTest

    # .................................................................
    #
    # def __init__(self):
    #     self.method_counter = 0
    #     self.field_counter = 0
    #     self.method_list = []
    #     self.field_list = []
    #
    # def enterFieldDeclaration(self, ctx:JavaParserLabeled.FieldDeclarationContext):
    #     self.field_counter += 1
    #     field_name = ctx.variableDeclarators().getText()
    #     self.field_list.append(field_name)
    #
    # def enterMethodDeclaration(self, ctx:JavaParserLabeled.MethodDeclarationContext):
    #     self.method_counter += 1
    #     method_name = ctx.IDENTIFIER().getText()
    #     self.method_list.append(method_name)

    # .................................................................

    # def enterClassDeclaration(self, ctx:JavaParserLabeled.ClassDeclarationContext):
    #     # print(ctx.getText())
    #     # print(ctx.IDENTIFIER())
    #     # print(ctx.IDENTIFIER().getText())
    #     # print(ctx)
    #     # ...............................................
    #     class_nmae = ctx.IDENTIFIER().getText()
    #     result = {}
    #     interfaces = []
    #     # print(ctx.typeList())
    #     # print(ctx.typeList().getText())
    #     for i in ctx.typeList().typeType():
    #         print(i.getText())
    #         interfaces.append(i.getText())
    #         result[class_nmae] = interfaces
    #         print(result)



def main():
    try:
        import understand as und
        from openunderstand.db.api import create_db
        from openunderstand.db.fill import main
        from openunderstand.db.models import ModelName
    except ImportError:
        print("Can not import understand")

    db = und.open("F:\Antlr\session 4\OpenUnderstand-master\openunderstand\analysis_passes\sample.txt")



    for ent in db.ents():
        for ref in ent.refs():
            if ref == "throw":
                res = []
                res.append("void")
                res.append(ent)
                res.append("throw")
                res.append(ref.ent())
                f = open("sample.txt", "a")
                f.write(' '.join(res))
                f.close()
                del res


    try:
        input_steam = FileStream("F:\Antlr\session 4\examples\sample.txt")
        lexer = JavaLexer(input_steam)
        tokens = CommonTokenStream(lexer)
        parser = JavaParserLabeled(tokens)
        tree = parser.compilationUnit()
        listener = Mylistener()
        walker = ParseTreeWalker()

        walker.walk(
            listener=listener,
            t=tree
        )
    except:
        print("")

    create_db(
            dbname="F:\Antlr\session 4\OpenUnderstand-master\openunderstand\analysis_passes\database.db",  # customize the path
            project_dir="F:\Antlr\session 4\OpenUnderstand-master\openunderstand\analysis_passes"  # customize the path
        )


    obj, has_created = ModelName.get_or_create(listener.field_list[0])


    # for ent in db.ents():
    #     print(ent, ent.kind(), sep=' | ')

    # app_class = db.lookup("Sample", "Class")
    # print(app_class)

    # ent = db.lookup("LocalDate", "Class")[0]
    # print(ent)
    #
    # print(ent, ent.kind())
    # print(ent, ent.simplename())
    # for ref in ent.refs():
    #     print(ref, ref.kind(), sep=' | ')

    # print(f"This file contains {listener.field_counter} fields and {listener.method_counter} methods.")
    #
    # print(listener.field_list)
    # print(listener.method_list)

    # f = open("sample.txt", "r")
    # for v in f:

        # res = {}
        # for key in listener.package_name:
        #     for value in listener.classes:
        #         # res[key] = value
        #         # listener.classes.remove(value)
        #         res["package_name"] = key
        #         res["classes"] = value
        #         break
        #
        # print(res)
        #
        # with open("sample.json", "w") as outfile:
        #     json.dump(res, outfile)
        #


        # print(f"This file contains {listener.field_counter} fields and {listener.method_counter} methods.")
        #
        # print(listener.field_list)
        # print(listener.method_list)

        # f = open("./Example.java", "r")
        # for v in f:
        #     if '//' not in v:
        #         f = open("./output.java", "a")
        #         f.write(v)
        #         f.close()

if __name__ == '__main__':
    main()

