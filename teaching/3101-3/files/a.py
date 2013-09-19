from b import B
class A:
  def __init__(self, ref):
    if isinstance(ref, B):
        self.ref = ref
