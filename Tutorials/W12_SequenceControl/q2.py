    def visitId(self,ctx,o):
        for symbol in o.sym:
            if ctx.name == symbol.name:
                if o.isLeft:
                    if isinstance(symbol.value.value, int):
                        return self.emit.emitWRITEVAR(symbol.name, symbol.mtype, symbol.value.value, o.frame), symbol.mtype
                    else:
                        return self.emit.emitPUTSTATIC(symbol.value.value + '.' + symbol.name, symbol.mtype, o.frame), symbol.mtype
                else:
                    if isinstance(symbol.value.value, int):
                        return self.emit.emitREADVAR(symbol.name, symbol.mtype, symbol.value.value, o.frame), symbol.mtype
                    else:
                        return self.emit.emitGETSTATIC(symbol.value.value + '.' + symbol.name, symbol.mtype, o.frame), symbol.mtype