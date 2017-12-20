function changeCase(identifier, targetCase){

  if (!identifier) return identifier;

  let sourceCase = '';
  if (!(identifier.match('_') || identifier.match(/[A-Z]/)))
    sourceCase = "kebab";
  else if (!(identifier.match('-') || identifier.match(/[A-Z]/)))
    sourceCase = "snake";
  else if (!(identifier.match('_') || identifier.match('-')))
    sourceCase = "camel"
  else
    sourceCase = undefined;

  if (sourceCase === undefined) return sourceCase;

  switch (targetCase){
    case "snake":
      if (sourceCase === 'camel')
        return identifier.replace(/([A-Z])/g, (s, m1) => '_' + m1.toLowerCase());
      else
        return identifier.replace(/-/g, '_');
      break;
    case "kebab":
      if (sourceCase === 'camel')
        return identifier.replace(/([A-Z])/g, (s, m1) => '-' + m1.toLowerCase());
      else
        return identifier.replace(/_/g, '-');
      break;
    case "camel":
      if (sourceCase === 'kebab')
        return identifier.replace(/-(\w)/g, (s, m1) => m1.toUpperCase());
      else
        return identifier.replace(/_(\w)/g, (s, m1) => m1.toUpperCase());
      break;
    default:
      return undefined;
  }
}